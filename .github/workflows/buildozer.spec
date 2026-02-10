[app]

# (str) आपके ऐप का नाम
title = Leo AI

# (str) पैकेज का नाम (बिना स्पेस के)
package.name = leoai

# (str) डोमेन नाम (यूनिक पहचान के लिए)
package.domain = org.leo

# (str) सोर्स कोड की लोकेशन
source.dir = .

# (list) कौन-कौन सी फाइलें ऐप में शामिल करनी हैं
source.include_exts = py,png,jpg,kv,atlas

# (str) ऐप का वर्शन
version = 0.1

# (list) सबसे जरूरी हिस्सा: ऐप को चलाने के लिए जरूरी लाइब्रेरीज़
requirements = python3, kivy, google-generativeai, requests, certifi, chardet, idna, urllib3

# (str) ऐप का ओरिएंटेशन (Portrait यानी सीधा या Landscape)
orientation = portrait

# (list) ऐप को कौन सी परमिशन चाहिए (Gemini के लिए इंटरनेट जरूरी है)
android.permissions = INTERNET

# (int) एंड्रॉइड API लेवल (33 या 34 रखें)
android.api = 33

# (int) कम से कम कौन से एंड्रॉइड वर्शन पर चलेगा
android.minapi = 21

# (str) ऐप का आइकन (अगर आपके पास icon.png है, वरना इसे छोड़ दें)
#icon.filename = %(source.dir)s/icon.png

# (list) आर्किटेक्चर (Modern फोन्स के लिए arm64-v8a जरूरी है)
android.archs = arm64-v8a, armeabi-v7a

# (bool) क्या आप चाहते हैं कि ऐप फुल स्क्रीन चले?
fullscreen = 0

# (list) बिल्डोजर को 'Root' एरर से बचाने के लिए सेटिंग्स (GitHub Actions के लिए)
p4a.branch = master

[buildozer]
# (int) लॉग लेवल (2 यानी सब कुछ विस्तार से दिखाओ)
log_level = 2

# (int) बिल्ड रुकने पर चेतावनी देना
warn_on_root = 1
