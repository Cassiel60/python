#!/usr/bin/python
#-*- coding:utf-8-*-

class Employee:
    empCount = 0

    def __init__(self,name,salary,sex):
        self.name=name
        self.salary=salary
        self.sex=sex
        Employee.empCount+=1

    def displaycount(self):
        print 'Total Employee %d' % Employee.empCount

    def displayEmployee(self):
        print "Name :",self.name ,", Salary :",self.salary, ", Sex :" ,self.sex
 
        

emp1=Employee('Zara',2000,'female')

emp2=Employee('Manni',5000,'male')

emp1.displayEmployee()
emp2.displayEmployee()

emp1.displaycount()


print "Total Employee % d" %Employee.empCount
