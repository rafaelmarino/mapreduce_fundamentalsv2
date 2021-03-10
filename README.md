# Hadoop MapReduce Exercises

Assignment for a graduate course on big data taken at McGill University---Winter, 2020.  
Follows Udacity's [Intro to Hadoop and MapReduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617)

## Repo structure

├── datasets  
│   ├── access_log.gz  
│   ├── forum_data.tar.gz  
│   └── purchases.txt.gz  
├── q1_purchases  
│   ├── A  
│   │   ├── q01a_answers.txt  
│   │   ├── q01a_driverprog.txt  
│   │   ├── q01a_mapper.py  
│   │   └── q01a_reducer.py  
│   ├── B  
│   │   ├── q01b_answers.txt  
│   │   ├── q01b_driverprog.txt  
│   │   ├── q01b_mapper.py  
│   │   └── q01b_reducer.py  
│   ├── C  
│   │   ├── q01c_answers.txt  
│   │   ├── q01c_driverprog.txt  
│   │   ├── q01c_mapper.py  
│   │   └── q01c_reducer.py  
│   ├── D  
│   │   ├── q01d_answers.txt  
│   │   ├── q01d_driverprog.txt  
│   │   ├── q01d_mapper.py  
│   │   └── q01d_reducer.py  
│   └── double_checking.ipynb  
├── q2_server_logs  
│   ├── A  
│   │   ├── q02a_answers.txt  
│   │   ├── q02a_driverprog.txt  
│   │   ├── q02a_mapper.py  
│   │   ├── q02a_notes.txt  
│   │   └── q02a_reducer.py  
│   ├── B  
│   │   ├── q02b_answers.txt  
│   │   ├── q02b_driverprog.txt  
│   │   ├── q02b_mapper.py  
│   │   └── q02b_reducer.py  
│   └── C  
│   ├── q02c_answers.txt  
│   ├── q02c_driverprog.txt  
│   ├── q02c_mapper.py  
│   └── q02c_reducer.py  
├── q3_forum_discussion  
│   ├── A  
│   │   ├── q03a_answers.txt  
│   │   ├── q03a_driverprog.txt  
│   │   ├── q03a_mapper.py  
│   │   └── q03a_reducer.py  
│   ├── B  
│   │   ├── q03b_answers.txt  
│   │   ├── q03b_driverprog.txt  
│   │   ├── q03b_mapper.py  
│   │   └── q03b_reducer.py  
│   ├── C  
│   │   ├── q03c_answers.txt  
│   │   ├── q03c_driverprog.txt  
│   │   ├── q03c_mapper.py  
│   │   └── q03c_reducer.py  
│   └── D  
│   ├── q03d_answers.txt  
│   ├── q03d_driverprog.txt  
│   ├── q03d_mapper.py  
│   └── q03d_reducer.py  
└── README.md

## Exercises

## Question 1

The file purchases.txt.gz is a zlib compressed text file which contains
sales information for one company with many stores. When uncompressed via gunzip
purchases.txt.gz, it has contents:  
[Date]\t[Time]\t[StoreLocation]\t[ProductType]\t[Amount]\t[PaymentMethod]

Please use MapReduce (any programming language) to answer the following questions:

```
(a) Provide a sales breakdown by store  
(b) Provide a sales breakdown by product category across all of the stores  
(c) Find the monetary value for the highest individual sale for each separate
store  
(d) Find the total sales values across all the stores and the total number of 
sales. You may assume there is only one reducer  
```

## Question 2

The data set we are using is an anonymized Web server log file from a public relations company whose clients were DVD distributors. The log file is called access_log.gz and it is compressed using GnuZip. So you’ll need to decompress it and then put it in HDFS. If you take a look at the file, you’ll see that each line represents a hit to the Web server. It includes the IP address which accessed the site, the date and time of the access, and the name of the page which was visited.

The logfile is in Common Log Format:  
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /a.htm HTTP/1.1" 200 10469  
%h %l %u %t "%r" %>s %b

Where:  
• % h is the IP address of the client  
• % l is identity of the client, or "-" if it’s unavailable  
• % u is username of the client, or "-" if it’s unavailable  
• % t is the time that the server finished processing the request. The format is
[day/month/year:hour:minute:second zone]  
• % r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.  
• % >s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org  
• % b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.

Please use MapReduce to do the following:

```
(a) Display the number of hits for each different file on the web site  
(b) Determine the number of hits to the site made by each different IP address  
(c) Find the most popular file on the web site. That is, the file whose path 
occurs most often in access_log.
```

## Question 3

In question you will work with discussion forum (also sometimes called discussion board) data. It is one type of user generated content that you can find all around the web. Most popular websites have some kind of a forum, and the things you will do in this project can transfer to other similar projects.

This particular dataset is taken from Udacity forums the first months after launch. Udacity forums are run on free, opensource software called OSQA, which was designed to be similar to the popular StackOverflow forums. The basic structure is - the forum has nodes. All nodes have a body and author_id. Top level nodes are called questions, and will also have a title and tags. Questions can have answers. Both questions and answers can have comments.

There are 2 files in the dataset. The first is forum_nodes.tsv, and that contains all forum questions and answers in one table. It was exported from the RDBMS by using tab as a separator, and enclosing all fields in doublequotes. You can find the field names in the first line of the file forum_node.tsv. The ones that are the most relevant to the task are:

• id: id of the node  
• title: title of the node. in case "node_type" is "answer" or "comment", this field will be empty  
• tagnames: space separated list of tags  
• author_id: id of the author  
• body: content of the post  
• node_type: type of the node, either "question", "answer" or "comment"  
• parent_id: node under which the post is located, will be empty for "questions"  
• abs_parent_id: top node where the post is located  
• added_at: date added

The second table is forum_users.tsv. It contains fields for:

• user_ptr_id : the id of the user.  
• reputation : the reputation earned when other users upvote their posts  
• the number of "gold", "silver" and "bronze" badges earned. The actual database has more fields in this table, like user name nickname, bio (if set) etc but we have removed this information here.  

```
(a) Find for each student what is the hour during which the student has posted
the most posts. Output from reducers should be
    author_id \t hours

If there is a tie please print the student-hour pairs on separate lines. The 
order in which these lines appear in your output does not matter.

You can ignore the time-zone offset for all times - for example in the 
following line:
    "2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

In order to find the hour posted, please use the date_added field and NOT the
last_activity_at field.
```
```
(b) We are interested to see if there is a correlation between the length of a 
post and the length of answers.

Write a mapreduce program that would process the forum_node data and output
the length of the post and the average answer (just answer, not comment)
length for each post. You will have to decide how to write both the mapper
and the reducer to get the required result.
```
```
(c) We are interested seeing what are the top tags used in posts. Write a
mapreduce program that would output Top 10 tags, ordered by the number of
questions they appear in. Please note that you should only look at tags
appearing in questions themselves (i.e. nodes with node_type "question"), not
on answers or comments.
```
```
(d) We might want to help students form study groups. But first we want
to see if there are already students on forums that communicate a lot between themselves.

As the first step for this analysis we have been tasked with writing a 
mapreduce program that for each forum thread (that is a question node with 
all it’s answers and comments) would give us a list of students that have 
posted there - either asked the question, answered a question or added a 
comment. If a student posted to that thread several times, they should be 
added to that list several times as well, to indicate intensity of 
communication.
```