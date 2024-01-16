#1 Naviagte back 
 #excercise: indexing and slicing

url = "https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv"


#use indexing and slicing to fill in the following output
#copy and paste is not allowed

file_name = url[-14:]
print(file_name) // 'ted-sample.csv'




protocol = url[0:5]
print (protocol) #https

host_name = url[8:18]
print(host_name) #'github.com'

#use string composition to construct http://github.com/ted-sample.csv
output = protocol + "://" + host_name + '/' + file_name