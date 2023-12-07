from flask import Flask
import os
import MySQLdb


#Criando conexão com o DB
db = MySQLdb.connect(
    host="aws.connect.psdb.cloud",
    user="brif3h2xssy0y808ptp4",
    passwd="pscale_pw_uzIYNxeewsAm7zDQiay8V5noWRThn0uveLKa1nWdX2K",
    db="luisao",
    autocommit=True,
    ssl_mode="VERIFY_IDENTITY",
    ssl={"ca": r"C:\Users\luisg\Downloads\myself\cacert.pem"}
)
