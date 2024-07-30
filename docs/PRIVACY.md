# Hush Line Privacy Policy

**Effective Date: March 11, 2024**

## Introduction

This Privacy Policy outlines our commitment to protecting the privacy and security of the personal information collected from users of our app. By using our app, you consent to the data practices described in this policy.

## Information Collection

- **User Provided Information:** We collect personal information that you provide to us, such as your username, display name, email address, and encrypted password. Additionally, we collect Two-Factor Authentication (2FA) data, SMTP settings, and PGP keys if you choose to provide them.
- **Automated Information Collection:** We use custom Nginx logging to remove IP addresses and country codes from access logs.

### Log Example
```
0.0.0.0 - - "GET /submit_message/scidsg HTTP/1.1" 200 929 "-"
0.0.0.0 - - "GET /static/style.css HTTP/1.1" 304 0 "-"
0.0.0.0 - - "GET /static/script.js HTTP/1.1" 304 0 "-"
0.0.0.0 - - "POST /submit_message/scidsg HTTP/1.1" 302 231 "-"
0.0.0.0 - - "GET /submit_message/scidsg HTTP/1.1" 200 973 "-"
0.0.0.0 - - "GET /static/style.css HTTP/1.1" 304 0 "-"
0.0.0.0 - - "GET /static/script.js HTTP/1.1" 304 0 "-"
```

## Use of Information

The information we collect is used for the following purposes:

- To provide and maintain our app's functionality, including user authentication, message encryption, and SMTP email services.

## Data Storage and Security

- **Data Encryption:** We use Fernet symmetric encryption to secure sensitive data such as password hashes and 2FA secrets. PGP keys are also encrypted for additional security.
- **Database Security:** User data is stored in a MySQL database with restricted access to protect against unauthorized access.
- **Form Handling and Validation:** We utilize Flask-WTF for secure form handling and validation, ensuring the integrity and confidentiality of user input.
- **Cryptography and Security Measures:** Our app employs advanced cryptography techniques (such as `pyotp` and `gnupg`) and Fernet encryption to enhance data security.
- **Server Security:** We use fail2ban to protect against brute-force attacks and UFW (Uncomplicated Firewall) for managing network traffic.
- **Data Retention:** We retain your information as long as your account is active or as needed to provide you services. After account deletion or prolonged inactivity, we may retain certain data for legal or operational purposes, typically not exceeding 90 days.

### DB Example Query
```
id: 1
username: scidsg
display_name: Science & Design
password_hash: gAAAAABlmgU-WeEuGr7b-HlwHJ5pIzxD3g9hLPStc8kUBZMiKyFVnj66Um6H4Sz2STfG6W8VBTP2zO2cG19ofqmdfQolx_Da6m_X3lHUajdlh1yp1alf_BoAoBvMxPUDkDRrrUWuaR1T0fJYeXY-C63ulfN6F2oCmQ==
totp_secret: gAAAAAAAAAAAWumslIWNS7FEEAjf6nFqyeamKYTf0dmwnIUIRaLTzDcgDHeHimST4Lb3eIUwu-8fRVT9kiiSb3igbh-tANjLEIQV2E8ohkEPwmCJ8_wYR3ediBsGaTWMQHaIykV3sznk
email: gAAAAAAAAAAAGyR8cJ03-MbSb7E3ozM10I_hDA4E22GmUxibQFLsI92lbKDwcMpXwGt_kZnJZgorMhpplbRPFHvytnL0aJOnrejkrua2YVwhrsuu0GwK8GA=
smtp_server: gAAAAAAAAAAA1SvRZLqFxdTPb0mTVdi9Hm6YJwnqItRNlcZKsJZGkSp55H4AkInkVblzyCyYuB0C4JCkzYVnuXQXt5TqTDiNPw==
smtp_port: 587
smtp_username: gAAAAAAAAAAASFNOr6xkrHtVMUTmcbzDKKAvWaGEXZstusPPrRKFTjgeBOXdFmClmxvZ50yU7uSXT2-yzhMqQS-yaSh7qJUSqxizMP36rxRhT_6qPuhECq0=
smtp_password: gAAAAAAAAAAAtJFpAFZkFcXbF2PfN9sDMinQ-GG0DO2-AO_2b9OeMtzlDwO5jPhZs-u0_hjjKip7b09r0QPAK89hfOuMsJOleG9HVif2sjiDiVDZj4_OyRY=
pgp_key: gAAAAAAAAAAAojyYZexHGNf_CRJhkSXz_QqZ45VAbN7XetrP5_xA81bJAuonMdpIxTVpB57wddZjLbY8gyZb4pDQ8aTntup93tCD99VKKYTpKSQyVe6K9CsRMx4YtB2E-rvfm78fuCgW0w1GGYCAUNI2hWZ_GvlMiZBkH8_p4FDIoN61WqPoVy1U2JasrJ3KJjhGaRTb4VQNUSai0crtUcXEMYZRYms9wGwin0bcygz8s9D2WQL7Iq-gggX1xOF4BpficvbBAd_ruddXtLKbDQLa_jylig_YaWrbc-qCjZEatpefl7yZVY1V7oXuuDHDAho8zn4o6tNgcBPW2KRBnhVI3N6QbCaCkuyE4I8VhXgvnXlZB8j4koB0k_lry8CzND83MMHDH1YS3InqZcPT9lUrKhGHxD2yVSwpUzNOrI8_V0V47UFwpstiSOCowfOLY2RTvol1G_005Lar9X3CnPruijSxMKEafd7SW_EP-iXn6ORE1wW2Hu63T3XCK6OR80kL6QgUIwLVsC_BRgJUq9TGFiE7mWdp7PDOFoSFiZtC2RbWOFqiBv10q9YazKlCi8MloWD6VcZc8rLPc-WOEpBlnqX38UgCGN5cHN2NJmm-dYJg7CP6VI0MlBwA1W04uQV82-fkIL4_hZv9785Zk7jk4fCYX3_g3UJgfVFRnbRjJj44V9i92B8kpDe6nKEhMJwozteHk2nIM-PkK-lF4kzJOzzzNSQOHkFy8H4-eYGQ7be-9aqYjHtcp7FAdOjtny2Vl3WaSBIGpy-65MHLy1Py67YB1qViWkJgmKrigO4RenB9s2c17SGy92I0cl92sXaCUQCgZtAQGDuPoqK5Dmb6LcVHQAHcQrVBaFpvrsyPfYzAcprRsGxWghdqMpoTzaeodSZmsmMU9LE3xzNqSrDYy-l3fcV9qh9c-4zRcNrsNNwq9_zvJBCBF3RqDFoet1otOeGmWMI-dBbhHoFpn8r7A3K1e9LoBEBte6yPH-7kuPJ6omtnSJooKGdQM_YOGUr9zEnLDi63lYPZp-Xxt3skaQUTIzKnsGSGAhC6VSHYTBWUU7yZEpNS0MbSI0wJKU2W5Edzgt5WgKJVX1_ey4-W519Zk-tiWAhXX-VYdUA6qw6RdEH9PTzV3tMhXBgoiPbtzZWD54saGWALQUzrb2pdLDrH-ArU3Kfof2TfN6tXeTeEp-2MVr-vtw5pe-UvdJ8f2Qa8L5P-RCf7em3IHnyD2r-hxBoY1WgHPlYd_mmyQVsjpJrBO6uFQhGOorWglM5r6yjFY2hPLjimVw1EvxhZgMwXbjgIr5Qx69xPmn0CHDyW7O4EWCbSho-4W6Ia_iHbFFZ3XMqVKO4bt4kxBHgJ2EFpXL-pTP_zkIjVj0hLFZWacysMP3HkfRVIufEzFy_kzPamMITD44FkxdVNCX2bAiUNdJ9D769ocUKHGZnei5hzA7XlBSXsJdlNkyqHJ61yZWCPjpEKlFydlog9NYGPlEbjPr1dTLyZbiU8oHSTJG5KNwJbe8ZkvNCDLp01KOIh6WQBldxWyo5ZXoTvUqTF6Zj2TkgeJgl08cFfVAq4WysY_ACUsFqWFJXTatdRDEXOFvSczdBN1wLHbgQv6YMBXso9RrUEYW6tKQT4rRIy6bKXLf7YLLCtftbEmS-XPeu11xRlgcfAVwxS5uYWKgYyOOGrWuu7XfwIWv7fRsYsbNsdtaZsCJW1IV2PJn6jrOPS0hNupSN6aR3C8SYXKNtDql23eFOZFHFcrbvhR0nEBPoeunyAPQQo3wBRNBI01PBxviHB67x-owe9ijIy8H4bwrMhlbdFuhvi1ayYQ_ol9YKxj4lfkGvYyuvmuSTk0pH0jgOIeRuM635k_k8o06544_h99QAihefGVM0tBaNHGj9GaGzX8NC0qiplONOZIZwqsZ746Kize7M6khMuXXXvEJOpUthT6432AaM8xSkDCbhNMD5kJDzNxbWPyU7iCi86av-amkR7U6_qrL4vKtd6cjGVfuJJJVnzzRljTEtveFwvRki0bgPdj39LTY4SK39zwTWLniagN0jLYVs1EPbw41BAyKC6Luct7E-1RsGYIPL71Nt7pX3sQ2NVP3nL3j1mRCujIm4CloT1ByQaQ7jsppTDWXZtWhiyYAxvVty_uXLf_psjhK8jrWnZ5l5EROUppdkd7OuaZDpc-HRjkGaTV4FKvIkhFXzrhXihg93jA5kfNStMyOxfZqqqzX1GjH6WFnFfRGFxf2UtgBBbOKzEZ90xajIhnSvfuzQ0YSR04HRUVMCCHlzku7-gjIKf8wS_TG56GlWBvg8VmEilHk8q653S24v05ZDM-ZlY-Rp2L_cMNxo8lQIlX9UdGPCEEDyN7zRNiePvkE8hJlpyhIsy28vPpJHCw3Qme6BoxM1AB56CezEjphKVw3ZnLK0K798fqVi9G_1EQJKL_MIorp0jJQN3lQgGE9NmVmYfEQ1Fx6a3kGQAl0wldOIARPQVWGMBztMDtK0CojClfgHjYsSaHo2FQbmqm-9gCdKV50YC_5qvdgjAcUwA5138hWC1UGOK79oiHbzdPMqPMdnFrpgK7WEmU5U04ehwaeVn9qt7U5VgqPx938BkMymydHuwYJSy5DXrdEiOFi_yD9OLP50h6dSBSdqbVljIOI7tcYXxEGE3xkVH0w6DPGGUILzs9DWJ1449DCU2tIPpXOhFg0NW33vhzp1oPMKFtjTVun6J2bRunXJruakhwaW9QMm5yRMfCDsYba0ITxQDaAN4H_VTv-4TepW98v8VQ-1opMY0-J3ZQOB_Vp_2omdBML43otUcOeeZ0iEbzt2xfO95ZWdLmrYRP0uFfyDdTHV1JjT4wvdIEZ1HGKDHXAqx_zL1hWwEILcOV2aC70YDTlICSg-kam1DyGLyo-1T284xpkau3BB7NcRL9cdwgDd--N3Oh4KAVNAx7GGoiBAQxzEaO6UvEY13GQnETlWGHfjtX6v2Q1VXpuFBxpSp0OUj8LW7iqbql0lY90FutwkfSWqCcEvw08Nuuz6WV0Qxh0XEbNhlHDHyJ2T3wyH3GM8bT6H0AImmbqgi2ztpu16DIGrcW5BJKMwqABlwFtfPtOvmlglNW9rMzVOYwwgQ_jhFHbeCFMx6qcFX4CSbqmfakjC_WLL7Oc9xD4TxPQOV_5VbS0_c5-Cl3LuU3b-q9P7VVvPE1Pc4fsbOKNa8OUglx2lk34y4VyjHvvLcopa3dnOkMiZjagUZ7NdFevBBwZMCL1c4tUhmfgMAphw3ahlm1zpQ8EBBtx5gT56Gk-MFKD5yfY2kjhwFkZIQLbISAHWN5OVPFtnyBllraOKFXUwRzDuRx8zTQbgNRNmd2iBVlS3XVj2GRmXGqEEDag_dE3UFkyC_JaUHUWSyvj62fxWnPor3z8iWWPfTkCxvhatLl9IWHFsBoR56hSW3nuF9EINyX2cPxZNfRNLKzATYDpsvod0lSxhO34aISh33e0K4YJCHnrek0-w14EVAVGQ2q8hH9HB8OHnpxumZ_0HcQH1zT6OqQ9wuDX3gL2NqHsMeyNKqIeF75Nh6ym01CAN5r57B-gPquATc5G-lkeAl1I8DS-AaZn8rq0pEK-gP_fDd_Kd-kSYAqVG3XA0IW8WcgwGwTI0wvfOVxTkfv0w7BeoTq5UcPJMCEHxLT35KLt66mjXZRpX8F_Jz32nvBgVsjlM9YyEnQ5WiRPblntS2Q-bcVCfzdrMKYZ5Zlq-EYiB10o-qPSvz5x2k2vD8Q3aa4unpWRVqG3AQB_QSdgzSY4NaBn4H6hWk32l3_CQo9JfTlEhbOb08lPv6iiTR84t_iqHvhzkLSpX_I3Rv1EgTvND_C81X3ALDbViJV5DgdqpPIf69kYTj0OLOx8WSeUVyDldFlb9q-xFKmbfLqC1IM6-zRCxl0Sh5urr6R3oAqCFmCvGj-gYOQigtP5w3AcbSN82Zuw6BLOjq0z0rSGMnMqsL6ldtYvUBD0ECgRgVhXNGTqFi79V9iUYmQc_9Bmdwvfy9nTsAAuxHz6zW7QX7L4wrKEzbs7TaX5e1rjdW2OuUhNdDzPNsgdgJAcz_NU7EtCB_dTKGDAvvLzmvTduThVGDXigBuC5sVC8x9991OtmGel-fGcrS9vvpCkhH2JyWo9IgzRgi-RlD-Aro_1ocnFoN94_8cC2tzMgju8faRksOayXbuTq0QIvWBQA8nH8bVv2CboYCMDt2O1glp3UJRghONjFaiQ8r7ypYREy2uFsQ847BESBksTizFs81tLOMYVVJVnNeDSlxMG9Ie2B1CxYcRvraUiqHeEcAZoISUQ61KTXaK9N7dugdiPi__rE6cSVcXk8FhXvD6yDEbF9-8TFfPj-PnarNzOUzXNPOtjYxgnd1xir2LuNk6ocKxUs4AZlhHcVB1UhS3bINN36n
is_verified: True
```

## Password Policy

- **Complexity Requirements:** Passwords must include uppercase and lowercase letters, digits, and a special character.
- **Length Requirements:** Passwords must be between 18 and 128 characters long.
- **Encryption:** Passwords are encrypted using `bcrypt` and securely stored.

## Additional Security Measures

- **Unattended Upgrades:** Our servers are configured with `unattended-upgrades` for important security patches.
- **Secure Server Configuration:** We use Nginx with privacy-preserving logging and HTTPS to ensure secure communication.
- **Tor Network Support:** The app supports access via the Tor network, providing additional anonymity options for users.
- **Fail2Ban and UFW:** We use `fail2ban` to monitor and mitigate unauthorized access attempts and `ufw` to manage network traffic, enhancing server security.

## Cookies and Tracking Technologies

Our app uses essential cookies to provide basic functionality and security features. These cookies do not track your activity on third-party websites or services. You can manage your cookie preferences through your browser settings.

## International Data Transfers

If you are accessing our app from outside the United States, please be aware that your information may be transferred to, stored, and processed by us and our service providers in the United States and other countries where our servers reside. We rely on recognized legal mechanisms such as Standard Contractual Clauses for such transfers.

## Data Sharing and Disclosure

We do not sell, rent, or lease our user data to third parties. However, we may share your data in the following situations:

- **Legal Compliance:** We may disclose your information if required by law or in response to legal requests by public authorities.
- **Service Providers:** We may employ third-party companies to facilitate our service, such as hosting providers, who are bound by strict confidentiality obligations.

## User Rights

You have rights over your personal data, including:

- **Access and Correction:** You can access and update your personal information via your account settings.
- **Deletion:** You can request the deletion of your account and associated data, subject to legal and operational considerations.
- **Data Portability:** You can request a copy of your data in a structured, commonly used, and machine-readable format.
- **Objection and Restriction:** You can object to or request the restriction of the processing of your personal data under certain circumstances.
- **Complaints:** You have the right to lodge a complaint with a supervisory authority if you believe your rights have been violated.

## Age Restrictions

Our app, Hush Line, is designed for users who are 18 years of age or older. Account creation and message reception are intended for individuals meeting this age requirement. We do not knowingly collect personal information from children under the age of 18 for these purposes. Should we become aware of such information having been collected, immediate steps will be taken to delete it.

### Contextual Exceptions for Users Under 18

Hush Line acknowledges its potential use in specific scenarios involving users under the age of 18, such as confidential student reporting systems within schools. While account holders (e.g., school administrators and counselors) are required to be 18 or older, individuals under 18 are permitted to send messages through Hush Line in these controlled environments for their safety and well-being.

### Implementation in Educational and Protective Environments

When implementing Hush Line within educational institutions or similar settings for use by minors, we uphold the following principles:

- **Institutional Responsibility:** It's crucial for institutions to ensure Hush Line's use complies with laws and regulations pertaining to minors' privacy and safety.
- **Parental Consent:** Appropriate consent from parents or guardians for minors' use of Hush Line should be secured, emphasizing transparency and accountability.
- **Privacy and Security with PGP Encryption:** We strongly recommend the use of PGP (Pretty Good Privacy) encryption for all messages sent through Hush Line, especially in contexts involving minors. PGP encryption helps secure the content of messages from unauthorized access, ensuring that sensitive information remains confidential and protected. This practice is vital for maintaining the privacy of all users and fostering a secure communication environment.

### Why PGP Encryption Matters

- **Enhanced Security:** PGP encryption provides a robust layer of security, safeguarding message content against potential interception or unauthorized access.
- **Trust and Confidentiality:** By encrypting messages, users can trust that their communications are kept confidential, which is particularly important in sensitive situations such as student reporting.
- **Compliance and Best Practices:** Using PGP encryption aligns with best practices for data protection and privacy, helping institutions comply with relevant regulations concerning the handling of personal information.

### Our Commitment

Hush Line commits to the privacy and protection of all users, advocating for responsible practices in the use of encryption and data security. We encourage educational institutions and organizations that engage with minors through Hush Line to prioritize these security measures. Our team is dedicated to providing support and guidance for integrating PGP encryption into your communication practices with Hush Line, ensuring a safe and private platform for all users.

## Third-Party Links

Our app may contain links to third-party websites or services that are not operated by us. This privacy policy does not apply to those third-party sites, and we encourage you to review their respective privacy policies.

## Data Breach Notification

In the event of a data breach that compromises the security, confidentiality, or integrity of your personal information, we will notify you promptly via email or prominent notice on our app, in compliance with applicable laws.

***

# Privacy Policy for the people under the GDPR

We provide this information according to the [EU Regulation 2016/679 (GDPR)](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679&from=EN) for those who consult the website https://hushline.app. Note that this information applies only to that website and not to other websites that the user may consult through links.

## Information to be provided according to Article 13 of the GDPR.
At the outset, it should be clear that the administrator of a Hushline instance is obliged, in their capacity as data controller, to provide information to the data subject according to Article 13 of the GDPR.

## Data controller

The data controller is **Glenn Sorrentino** - **glenn@scidsg.org**.

## What data is collected.

(a) Registration: username, password, and email;
(b) Access: IP address, username, password, and email.


## The purposes of the processing.

The purpose is to consult the website and use the services provided.

A) Consult the website. Accessing this website and requesting to register as a user means the user gave consent. Hence, the processing of personal data is based on consent - according to Article 6, par. 1, letter a) of EU Regulation 2016/679 - expressed by the user by browsing this website and its consultation, thus accepting this information. Consent is optional, and the user can withdraw at any time by request sent by email to [**email address**], specifying that, in this case, whether the user does not consent, they cannot consult this website, either register or remain as a registered user.
B) Services provided. The purposes are also related to accessing the services we provide. In that case, the legal basis is the contract to which the data subject is party or in order to take steps at the request of the data subject prior to entering into a contract.
t
## Legal basis for the processing

Regarding the purposes related to letter A) of the previous point, the data subject has given consent to the processing of his or her personal data for one or more specific purposes, according to Article 6, par. 1, letter a) of EU Regulation 2016/679, in compliance with the provisions of the same Regulation.
Regarding the purposes related to letter A) of the previous point, the processing of personal data is necessary for the performance of a contract to which the data subject is party or in order to take steps at the request of the data subject prior to entering into a contract, according to Article 6, par. 1, letter b) of EU Regulation 2016/679, in compliance with the provisions of the same Regulation. 

## Processing of data

### _Browsing data_

The user (data subject) can access this website and navigate through a web browser. Some data are necessary for surfing the Internet and could identify users through processing and association with data held by third parties. In particular, we intend to refer to the IP addresses or domain names of the computers used by users connecting to this website, the addresses in URI (Uniform Resource Identifier) notation of the requested resources, the time of the request, etc. We could use these data uniquely for anonymous statistical information on the use of the website and check its correct functioning, which is deleted immediately after processing. We could use data for any responsibility in the hypothesis of computer crimes connected to this website. Data relating to those who have submitted requests to [**Hushline**] using the tools on this website are stored for no more than seven days, however, for the time necessary to provide the answers and for any need to ascertain part of the judicial authority.

### _Data communicated by users_

The optional, explicit, and voluntary sending of electronic mail to the [**Hush Line**] addresses involves the acquisition of the sender's address necessary for the replies and any other personal data contained in the message. These data are processed to respond to messages sent and handle any related requests. Failure to provide personal data for communications with [**Hush Line**] or send any requests will prevent evading them. We store data for the time strictly necessary for the purposes related to data processing.

## Cookies

The only cookies present are only **functional ones** and, therefore, no profiling or tracking activities.

**Thus, this site does not use cookies other than functional cookies solely for the functional purposes described above, and their installation does not require the user's consent**.

### What are cookies?

Cookies (small text files that the visited website sends to your device, where they are then stored to be re-transmitted to the same website at the next visit) can be _permanent_ or _session_, "_First-party_" (site or domain of origin), or "_Third-party_" (from third parties). Persistent cookies consist of a text file sent from a web server to a web browser. Once stored by the browser, it remains valid until the scheduled expiration date (unless the visitor deletes it before the time mentioned above). Session cookies expire at the end of the session or when the user closes the web browser. "_First-party_" cookies are those set by this site; "_Third-party_" cookies are of a different domain than this one, and they are set up because they use functions managed by third parties. Our website uses the following cookies:

_Session cookies_ (not stored permanently on the user's computer and disappear when the browser is closed) and are strictly limited to the transmission of session identifiers (consisting of random numbers generated by the server) necessary to allow safe browsing and efficiency of the site. Session cookies used on this site avoid using other technologies that could compromise the privacy of users' browsing and do not allow the acquisition of personal data.

It is, however, possible for the user to set cookies from the "Preferences" of the browser used and eventually automatically refuse the receipt of cookies by activating the appropriate option: the non-use of technical cookies, however, could involve technical difficulties of interaction with this website.

You can find instructions for disabling cookies on the following web pages:

- [Mozilla Firefox](https://support.mozilla.org/en-US/kb/enable-and-disable-cookies-website-preferences)
- [Microsoft Internet Explorer](https://support.microsoft.com/ha-latn-ng/help/17442/windows-internet-explorer-delete-manage-cookies)
- [Microsoft Edge](https://support.microsoft.com/en-us/help/4468242/microsoft-edge-browsing-data-and-privacy-microsoft-privacy)
- [Google Chrome](https://support.google.com/chrome/answer/95647?co=GENIE.Platform%3DDesktop&hl=en-GB)
- [Opera](https://help.opera.com/en/latest/security-and-privacy/)
- [Apple Safari](https://support.apple.com/lv-lv/HT201265)

## Data recipients

We do not communicate personal data collected from this website following its consultation to recipients or categories of recipients.

## Period for storing personal data

Apart from what is specified above, the data collected by this website during its operation are stored for the time strictly necessary for the activities specified. The data will be deleted or anonymized at the expiry date unless there are no further purposes for storing it.

## Transferring personal data to a third country or international organization

If the Hushline instance is installed on a server within the European Economic Area (EEA), the data controller does not transfer data outside the EEA.

Users registered on an instance are always solely responsible for their activities.

There is no transfer outside the SEE when registered users on an instance within the same EEA perform activities on the same server (instance). For example, our instance (https://hushline.app) is located in [**TBD**] and thus within the EEA.

## Security measures

Visitors' or users' data are processed lawfully and correctly by adopting appropriate security measures to prevent unauthorized access, disclosure, modification, or unauthorized destruction of data. Your data in the communication session with this website are protected by a Secure Sockets Layer (SSL) certificate that uses a cryptographic presentation protocol to encrypt the information. In addition to the controller, in some cases, authorized persons may have access to the data as involved in the organization of the website or external subjects (such as third-party technical service providers and hosting providers).

## Data subjects' rights

This website's users (data subject) may exercise the rights according to Articles 15 to 22 of EU Regulation 2016/679. You can lodge all requests to exercise these rights by writing to **hushline@scidsg.org**.

## Right to lodge a complaint

Whether a data subject considers that the processing of personal data relating to him or her as performed via this website infringes the Regulation, he or she has the right to lodge a complaint with the Garante according to Article 77 of the EU Regulation 2016/679.

***

## Changes to Privacy Policy

We reserve the right to modify this policy at any time. We will notify you of any changes by posting the new policy on this page and updating the "Effective Date" at the top of this policy.

## Contact Us

If you have any questions about this Privacy Policy, please contact us at [https://tips.hushline.app/submit_message/scidsg](https://tips.hushline.app/submit_message/scidsg).
