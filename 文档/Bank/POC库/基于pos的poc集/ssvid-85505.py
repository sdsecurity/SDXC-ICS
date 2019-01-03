?
Huawei Technologies eSpace Meeting Service 1.0.0.23 Local Privilege Escalation


Vendor: Huawei Technologies Co., Ltd.
Product web page: http://www.huawei.com
Affected version: 1.0.0.23 (V100R001C03SPC201B050)

Summary: Huawei&#39;s eSpace Meeting solution fully meets the needs of enterprise
customers for an integrated daily collaboration system by integrating the
conference server, conference video terminal, conference user authorization,
and teleconference.

Desc: The application is vulnerable to an elevation of privileges vulnerability
which can be used by a simple user that can change the executable file with a
binary of choice. The vulnerability exist due to the improper permissions, with
the &#39;F&#39; flag (full) for the &#39;Users&#39; group, for the &#39;eMservice.exe&#39; binary file.
The service is installed by default to start on system boot with LocalSystem
privileges. Attackers can replace the binary with their rootkit, and on reboot
they get SYSTEM privileges.

Tested on: Microsoft Windows 7 Professional SP1 (EN)


Vulnerbility discovered by Gjoko &#39;LiquidWorm&#39; Krstic
                           @zeroscience


Advisory ID: ZSL-2014-5171
Advisory URL: http://www.zeroscience.mk/en/vulnerabilities/ZSL-2014-5171.php

Huawei ID: Huawei-SA-20140310-01
Huawei Advisory: http://www.huawei.com/en/security/psirt/security-bulletins/security-advisories/hw-329170.htm



18.01.2014

------------------------------------

C:\&#62;sc qc eSpaceMeeting
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: eSpaceMeeting
        TYPE               : 110  WIN32_OWN_PROCESS (interactive)
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\ProgramData\eSpaceMeeting\eMservice.exe
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : eSpaceMeeting
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem

C:\&#62;icacls ProgramData\eSpaceMeeting\eMservice.exe
ProgramData\eSpaceMeeting\eMservice.exe BUILTIN\Users:(I)(F)
                                        NT AUTHORITY\SYSTEM:(I)(F)
                                        BUILTIN\Administrators:(I)(F)

Successfully processed 1 files; Failed processing 0 files

C:\&#62;

------------------------------------
