# Databricks notebook source
region_list = ["Asia", "Europe"]

dbutils.jobs.taskValues.set(key="regions", value=region_list)