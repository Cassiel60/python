#!/usr/bin/env python
#-*- coding: utf-8 -*-
#title           :calculate_sentence_distance.py
#description     :calculate the distance of the sentences in each paper
#author          :Huamei Li
#date            :2017-08-18
#type            :script
#python_version  :2.7

import os
import sys
import glob
import re
import time
import textract
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def read_pdf(pdf_files):
	pdf_files, corups = pdf_files if isinstance(pdf_files, list) else [pdf_files], []
	
	for pdf_file in pdf_files:
		if pdf_file.lower().endswith('pdf'):
			text = re.split('\r\n|\n', textract.process(pdf_file))
		else:
			text = re.split('\r\n|\n', open(pdf_file))
		tmp_res, flag = [], 0
		for line in text:			
			if (not line.strip().endswith('.')) or (not line.strip()): continue
			if len(line) < 300 and (':' in line or re.search('\d+-\d+', line)): flag += 1
			else:
				flag = 0
			if flag is 4:
				tmp_res = tmp_res[0 : -3]
				break
			line = line.replace('  ', ' ')
			if line[-1] == '.': line += ' '
			tmp_res.append(line)
		
		text = ''.join(tmp_res).split('. ')	
		[corups.append((pdf_file.split(os.sep)[-1].rsplit('.', 1)[0], re.sub('\r\n|\n', '', line))) for line in text]
	
	return corups
	
def parse_db(db_dir):
	if os.path.isfile(db_dir):
		db = [db_dir]
	else:
		db = glob.glob('{}/*.pdf'.format(db_dir))
		
	db_corups = read_pdf(db)
	return db_corups
	
def find_similar(tfidf_matrix, index, top_n = 5):
    cosine_similarities  = linear_kernel(tfidf_matrix[index:index+1], tfidf_matrix).flatten()
    related_docs_indices = [i for i in cosine_similarities.argsort()[::-1] if i != index]
    return [(index, cosine_similarities[index]) for index in related_docs_indices][0:top_n]
	
def create_outfiles(args):
	file_names = [fil.split(os.sep)[-1].rsplit('.', 1)[0] for fil in args.query_papers]
	out_files  = [os.path.join(args.output, fil + '_' + args.prefix + '_' + str(args.cutoff)) for fil in file_names]
	handles    = [open(fil, 'w') for fil in out_files]
	return handles

def calc_ratio(args):
	start = time.time()
	print >> sys.stderr, '[INFO] reading query paper'
	query_corups = read_pdf(args.query_papers)
	print >> sys.stderr, '[INFO] reading hits paper'
	db_corups    = parse_db(args.dbdir)
	handles      = create_outfiles(args)
	conts        = [cont for file, cont in db_corups]
	print >> sys.stderr, '[INFO] calculate the similary between the sentences'
	
	for kk, content in enumerate(query_corups):
		print >> sys.stderr, '[INFO] index {}: {}'.format(kk, content[1])
		if len(content[1].split()) < args.minlen: continue
		db_corups.insert(0, content)
		conts.insert(0, content[1])
		tf           = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')
		tfidf_matrix = tf.fit_transform(conts)
		similary_res = find_similar(tfidf_matrix, 0, top_n=args.maxnum)
		score_higest = similary_res[0][1]
		if score_higest < args.cutoff: 
			db_corups.pop(0)
			conts.pop(0)
			continue
		fp = [fp for fp in handles if content[0] in fp.name][0]
		fp.write('Query    = ' + content[1].strip() + '\n\n' ) 
		for ind, res in enumerate(similary_res):	
			index, score = res 
			if score < args.cutoff: break
			fp.write('Hit      = ' + db_corups[index][0] + '.pdf\n')
			fp.write('Score    = ' + str(score) + '\n')
			fp.write('Sentence = ' + db_corups[index][1].strip())
			fp.write('\n\n') if ind <> len(similary_res) - 1 else fp.write('\n')

		fp.write('\n\n//************************************************\n')
		db_corups.pop(0)
		conts.pop(0)
	print >> sys.stderr, '[INFO] task finish, consume {} seconds'.format(time.time() - start)

def main():
	parser = argparse.ArgumentParser(description="Given a PDF paper as input")
	parser.add_argument('query_papers', nargs='+')
	parser.add_argument('--dbdir' , '-d', help='database paper directory', type=str)
	parser.add_argument('--cutoff', '-c', help='cutoff value of similarity (default: 0.40)', type=float, default=0.40)
	parser.add_argument('--maxnum', '-m', help='max number of the highest sentences (default: 5)', type=int, default=5)
	parser.add_argument('--minlen', '-l', help='min length of the sentence (default: 10)', type=int, default=10)
	parser.add_argument('--prefix', '-p', help='prefix name of the output file (default: similar_ratio)', type=str, default='similar_ratio')
	parser.add_argument('--output', '-o', help='output directory (default: ./)', type=str, default='./')
	args = parser.parse_args()
	
	calc_ratio(args)
		
if __name__ == '__main__':
	sys.exit(main())
