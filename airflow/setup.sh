#!/usr/bin/env bash
# $AIRFLOW_HOME:
# ~/airflow
# airflow.cfg (in ~/airflow) dag folder:
# dags_folder = /home/ryan/airflow/dags
set -xoue pipefail
cp main.py ~/airflow/dags/
