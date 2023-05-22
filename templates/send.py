from flask import Flask
import psycopg2, 

conn = psycopg2.connect(
    dbname="postgress",
    user="shoc@choc.us", 
    password="JustKeepSwimming",
    host="pg_admin", 
    port="localhost:3031"
)
