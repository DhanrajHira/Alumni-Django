from django.shortcuts import render
from django.http import HttpResponse
from . import Sqplite as sqp
import sqlite3 as sql



def addRecord(request):
	if request.method == "POST":
		data = request.POST
		backend = sqp.Sqplite('database.db', onOpen = '''alumni (name VARCHAR(50), adminno INTEGER, 
		fathersname VARCHAR(50), mothersname VARCHAR(50),
		class INTEGER, phonenumber VARCHAR(50), age INTEGER,
		gender VARCHAR(10), house VARCHAR(50), adminyear VARCHAR(10),
		address VARCHAR(100))''')
		backend.insert('alumni', datamap= data, fieldnames=['name','adminno', 'fathersname', 'mothersname'
		,'class','phonenumber','age','gender', 'house', 'adminyear', 'address'])
	return render(request, 'alumni/addRecord.html')

def home(request):
	if request.method == 'POST':
		data = request.POST
		database = sqp.Sqplite('database.db', onOpen='')
		results = database.query(tablename = 'alumni', where='{0} = \'{1}\''.format(data['searchby'], data['searchfor'])) 
		return render(request, 'alumni/recordList.html', {'results': results})	
	return render(request, 'alumni/Home.html')

def allRecords(request):
	database = sqp.Sqplite('database.db', onOpen='')
	results = database.query(tablename = 'alumni')
	return render(request, 'alumni/recordList.html', {'results': results})

def deleteRecord(request):
	if request.method == 'POST':
		data = request.POST
		todelete = data['deleteadminno']
		database = sqp.Sqplite('database.db', onOpen='')
		database.delete('alumni', where = ' adminno = \'{0}\''.format(todelete))
		response = allRecords(request)
		return response
	return render(request, 'alumni/deleteRecord.html')