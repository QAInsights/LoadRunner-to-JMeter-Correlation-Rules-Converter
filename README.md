[![contributions welcome](https://img.shields.io/badge/contributions-welcome-1EAEDB)]()
[![saythanks](https://img.shields.io/badge/say-thanks-1EAEDB.svg)](https://saythanks.io/to/catch.nkn%40gmail.com)
[![](https://img.shields.io/badge/license-MIT-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://qainsights.com)
[![](https://img.shields.io/badge/%E2%9D%A4-QAInsights-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://qainsights.com)
[![](https://img.shields.io/badge/%E2%9D%A4-YouTube%20Channel-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://www.youtube.com/user/QAInsights?sub_confirmation=1)
[![](https://img.shields.io/badge/donate-paypal-1EAEDB)](https://www.paypal.com/paypalme/)

# LoadRunner to JMeter Correlation Rules Converter 🛠

## TLDR ⚡

From *.cor to *.json. Period.

## Overview 💡

This is a simple Python utility which will help you to convert your LoadRunner Correlation Rules to JMeter Correlation Rules.

## Prerequisites 🚩

* LoadRunner Correlation Rules (*.cor)
* JMeter Plugin Manager w/ Blazemeter's Correlation Recorder plugin
* Python

## How to use this repository? 🏃‍♂️

* Clone this repo
* Install the dependencies using
`pip install -r requirements.txt`
* cd into the repo
* Issue the below command:  
`python app.py -f <your-LoadRunner-Correlation-File>`  
e.g. `python app.py -f LR.cor`
* It will prompt to enter the details, if you are lazy 🐢 like me just keep hitting the enter key. After few hits, you will get a template and repository JSON as shown below.  

![Output](/assets/Output.jpg)

