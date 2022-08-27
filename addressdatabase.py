# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 11:07:58 2022

@author: SARKAR
"""
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
 

SessionLocal = sessionmaker(autocommit=False , autoflaush = False , bind=engine )
Base= declarative_base()
























































