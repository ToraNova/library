#!/bin/bash

#backs up a user's crontab

crontab -l > $(date +%y-%m-%d-bak.crontab)
