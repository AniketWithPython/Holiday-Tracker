`OPERATIONAL`

Holiday Tracker for Microsoft® Windows™

My first GUI and API based application<br><br>
![image](https://user-images.githubusercontent.com/98256334/150673288-d6c6d958-e63f-4658-b2ee-a2a85a5432c9.png)

<br><br>
Notes:<br>
* Can be used as startup application (Place app/shortcut in Startup folder by typing `shell:startup` in Run)
* Always on top window
* The number in the bracket represents the status code

<br><br>
List of status codes and their meanings:
* `200:Success` Everything went smooth.
* `401:Unauthorized` Missing or incorrect API token in header.
* `422:Un-processable Entity` Meaning something with the message isn’t quite right, this could be malformed JSON or incorrect fields. In this case, the response body contains JSON with an API error code and message containing details on what went wrong.
* `500:Internal Server Error` This is an issue with Calendarific's servers processing your request. In most cases the message is lost during the process, and we are notified so that we can investigate the issue.
* `503:Service Unavailable` During planned service outages, Calendarific API services will return this HTTP response and associated JSON body.
* `429:Too Many Requests` API limits reached.
* `600:Maintenance` The Calendarific API is offline for maintenance.
* `601:Unauthorized` Missing or incorrect API token.
* `602:Invalid Query Parameters`
* `603:Authorized Subscription Level Required`

<br><br>
API used: [https://calendarific.com/](https://calendarific.com/)

[Link To Software](https://drive.google.com/drive/folders/1k6Us2RrQFFCdYwpc_sSlI5zt-bFAuZND?usp=sharing)


> Holidays OP™ For Microsoft® Windows™ © 2022 Aniket Maity, All Rights Reserved

> Calendarific™ API Copyright © 2022 HATCHSQUARE Technologies LLC, All rights reserved. All other domain, brand information and trademarks are the registered trademarks of their respective owners
