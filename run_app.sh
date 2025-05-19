#!/bin/bash
export $(cat .env | xargs)
streamlit run app/main.py
