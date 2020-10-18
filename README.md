[![contributions welcome](https://img.shields.io/badge/contributions-welcome-1EAEDB)]()
[![saythanks](https://img.shields.io/badge/say-thanks-1EAEDB.svg)](https://saythanks.io/to/catch.nkn%40gmail.com)
[![](https://img.shields.io/badge/license-MIT-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://qainsights.com)
[![](https://img.shields.io/badge/%E2%9D%A4-QAInsights-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://qainsights.com)
[![](https://img.shields.io/badge/%E2%9D%A4-YouTube%20Channel-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://www.youtube.com/user/QAInsights?sub_confirmation=1)
[![](https://img.shields.io/badge/donate-paypal-1EAEDB)](https://www.paypal.com/paypalme/)

![Banner](/assets/00-Banner.jpg)

# LoadRunner to JMeter Correlation Rules Converter 🛠

## TLDR ⚡

From *.cor to *.json. Period.

## Overview 💡

This is a simple Python utility which will help you to convert your LoadRunner Correlation Rules to JMeter Correlation Rules.

## Prerequisites 🚩

* LoadRunner Correlation Rules (*.cor)
* JMeter Plugin Manager w/ Blazemeter's Correlation Recorder plugin
* Python 🐍

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

## Aftermath 🌪

After generating the JSON files, you have to follow the below steps to utilize it in JMeter.

* Place the folder where it is accessible, e.g. GitHub Repo
* Add `bzm - Correlation Recorder` to your JMeter test plan
* Click on `Load Template`

![00-Load](/assets/00-Load.jpg)

* Click on `Config`

![10-Templates-Manager](/assets/10-Templates-Manager.jpg)

* Enter unique `Id` and `URL` as shown below.

![20-Repo-Manage](/assets/20-Repo-Manager.jpg)

* If all is well, you will get the below success message.

![30-Repo-Success](/assets/30-Repo-Success.jpg)

* You could see your rules have been loaded in the `Templates Manager`

![40-Rules-Loaded](/assets/40-Rules-Loaded.jpg)

* Click on the rule which you would like to install and then click on `Install`

![50-Install-Rule](/assets/50-Install-Rule.jpg)

* You will get success message as shown below.

![60-Install-Success](/assets/60-Install-Success.jpg)

* To load the rule, click on `Load`

![70-Load-Rule](/assets/70-Load-Rule.jpg)

* You could see your LoadRunner Rules in JMeter.

![80-Loaded-Rules](/assets/80-Loaded-Rules.jpg)

> After loading the rules, you will have to fill the `Match Number, Group Number, Correlation Replacement` etc. 

## Tested with 🔨

This utility has been tested with:

* Micro Focus LoadRunner 2020 SP 2
* Apache JMeter 5.3
* Blazemeter Correlation Recorder 1.1

## License 🔒

MIT

## Contributions 💙

All contributions welcome. Please submit a PR.
