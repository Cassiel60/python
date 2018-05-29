#-*- coding:utf-8-*-
import sys,os
sys.path.append('../')
import pandas as pd
import paramiko
import collection
from analysis.modules.medical_public import unicodeToUtf8

def parseRNASeqConfig(configInfo):
  configInfo['baseInfo']['sampleinfo']=os.path.join(configInfo['baseInfo']['inputdir'],
                                                    configInfo['baseInfo']['sampleinfo'])
  configInfo['baseInfo']['outdir']    =os.path.join(['configInfo']['outdir'],
                                                    ['configInfo']['Issue'])
  configInfo['RNA_Seq']['db_genes']	  =os.path.join(['configInfo']['database_dir'],
                                                     configInfo['RNA_Seq']['db_genes'])
  outdir = configInfo['baseInfo']['outdir']
  1 if os.path.exists(outdir) else os.makedirs(outdir) 
  
  return configInfo
  
def parseSampleInfos(snFil):
  df        =unicodeToUtf8(pd.read_excel(snFil,sheetname=0))
  barcodeDf = df.loc[df['Name']=='Barcode Name']
  colNames  = df.columns
  barcodeLst= barcodeDf[colNames[2:]].values.tolist()[0]
  barcodeDic= dict(zip(colNames[2:],barcodeLst))
  
  timeDf    = df.loc[df['Name']=='Time']
  timeLst   = timeDf[colNames[2:]].values.tolist()[0]
  timeSerie   = dict(zip(colNames[2:],timeLst))
  
  return df ,barcodeDic,timeSerie
  
def download_dir(remoteDir, localDir, sftp):
  filterKeys  = ('bam','sam','bai','junction','htm')
  dirItems =sftp.listdir_attr(remoteDir)
  os.path.exists(localDir) or os.path.makedirs(loaclDir)
  for item in dirItems:
    remotePath = remoteDir + '/' + item.filname
	if '_' not in item.filename:
	  fmtFilName=item.filename
	else:
	  fmtFilName='_'.join(item.filename.split('_')[0:2]+\
	                '.'+'.'.join(item.filename.split('.')[-2:])
	localpath   = os.path.join(loaclDir , fmtFilName)
	try:
	  sftp.listdir_arrt(remotePath)
	  download_dir(remoteDir, localDir, sftp)
	except:
	  if remotePath.endwith(filterKeys): continue
	  sftp.get(remotePath,localpath)
	  print>>sys.stdeer,'[INFO] Download {} success!'.format(fmtFilName)
  return sftp
  
def downloadServer(barcodeDic,configInfo,ip,username,pwd,port=22):
  localDir   = configInfo['baseInfo']['inputdir']
  remoteDir  = configInfo['Server']['path']
  transport  = paramiko.Transport ((ip,port))
  transport.connect(username=username,password=pwd)
  sftp       = paramiko.SFTPClient.from_transport(transport)
  for name in barcodeDic:
    barcodeLst = barcodeDic[name].split(',')
	for barcode in barcodeLst:
	  remotePath = remoteDir + '/' + barcode
	  localpath =os.path.join(loaclDir,barcode)
	  1 if os.path.join.exists(localpath) else os.mkdir(localpath)
      download_dir(remotePath,localpath,sftp)
  transport,close()
  print >>sys.stdeer,'[INFO] Download total tesults from PGM server success'  
  return 0
  
def createCustomResDir(barcodeDic,outdir):
  for key in barcodeDic:
    outPath = os.path.join(outdir , key)
	1 if os.path.exists(outPath) else os.mkdir (outPath)
  return 0
  
def writeFPKM(fpkmFil,geneDb,results):
  resDict= collections.defaultdict()
  with open(fpkmFil,'r') as fpRead :
  header =fpRead.readline()
  index1 =header.split('\t').index('FPKM')
  index2 =header.split('\t').index('gene_short_name')
  for line in fpRead:
    if not in line: continue
	lineFmt =line.strip().split('\t')
	resDict[lineFmt[index2]]= line[index1]
  [results[gene].append(resDict[gene]) if gene in resDict else results[gene].append(0) for gene in geneDb]
  return results
  
def getFPKM(barcodeDic,customInfo,geneDb,timeSerie,suffix='genes.fpkm_tracking'):
  inputDir = customInfos['baseInfo']['inputdir']
  outputdir   = customInfos['baseInfo']['outdir']
  for name in barcodeDic:
    outPath = os.path.join(outputdir,name)
	results = collection.defaultdict(list)
  