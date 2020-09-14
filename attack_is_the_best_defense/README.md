# Attack is the best defense

## Resources:books:
Read or watch:
* [Network sniffing](https://intranet.hbtn.io/rltoken/0LIY07HGzUWgldJicE7iCQ)
* [ARP spoofing](https://intranet.hbtn.io/rltoken/5lwTtJQfvyQQsqyjkmi6JA)
* [Connect to SendGrid’s SMTP relay using telnet](https://intranet.hbtn.io/rltoken/ItMk1JBBHrit1IM9KFXS3A)
* [What is Docker and why is it popular?](https://intranet.hbtn.io/rltoken/WSPfahVAoZLfsIVa0mDyeQ)
* [Dictionary attack](https://intranet.hbtn.io/rltoken/nxnO-3amDO8L_BbFI4KOYw)
* [How to Send an SMTP Email - using telnet](https://sendgrid.com/docs/for-developers/sending-email/getting-started-smtp/)

---
## Learning Objectives:bulb:
What did I learn from this project:

* tcpdump
* hydra
* telnet
* docker

---

### [0. ARP spoofing and sniffing unencrypted traffic](./0-sniffing)
* Security is a vast topic, and network security is an important part of it. A lot of very sensitive information goes over networks that are used by many people, and some people might have bad intentions. Traffic going through a network can be intercepted by a malicious machine pretending to be another network device. Once the traffic is redirected to the malicious machine, the hacker can keep a copy of it and analyze it for potential interesting information. It is important to note that the traffic must then be forwarded to the actual device it was supposed to go (so that users and the system keep going as if nothing happened).

Any information that is not encrypted and sniffed by an attacker can be seen by the attacker - that could be your email password or credit card information. While today’s network security is much stronger than it used to be, there are still some legacy systems that are using unencrypted communication means. A popular one is telnet.

In this project, we will not go over ARP spoofing, but we’ll start by sniffing unencrypted traffic and getting information out of it.

Sendgrid offers is an emailing service that provides state of the art secure system to send emails, but also supports a legacy unsecured way: telnet. You can create an account for free, which is what I did, and send an email using telnet:

* telnet smtp.sendgrid.net 587

* I wrote the script user_authenticating_into_server that performs the authentication steps that I just showed above. Your mission is to execute user_authenticating_into_server locally on your machine and, using tcpdump, sniff the network to find my password. Once you find it, paste the password in your answer file. This script will not work on a Docker container or Mac OS, use your Ubuntu vagrant machine or any other Linux machine.

You can download the script user_authenticating_into_server here (https://intranet.hbtn.io/rltoken/GzCvsJxgywK6TKkfwTF3RQ)

DISCLAIMER: you will probably see Authentication failed: Bad username / password in the tcpdump trace. It’s normal, we deleted the user to our Sendgrid account. You can’t verify the password found via Sendgrid, only the correction system can!


### [1. Dictionary attack](./1-dictionary_attack)
* Password-based authentication systems can be easily broken by using a dictionary attack (you’ll have to find your own password dictionary). Let’s try it on an SSH account.

---

## Author

* [GitHub - Julian Franco Rua](https://github.com/julianfrancor)

* [LinkedIn - Julian Franco Rua](https://www.linkedin.com/in/julianfrancor/)
