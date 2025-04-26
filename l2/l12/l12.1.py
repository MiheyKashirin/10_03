import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file,'r','utf-8') as file:
        html=file.read()

    html=re.sub(r'<script.*?>.*?</script>','',html,flags=re.DOTALL)
    html = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.DOTALL)
    html = re.sub(r'<link.*?>', '', html, flags=re.DOTALL)
    html = re.sub(r'<meta.*?>', '', html, flags=re.DOTALL)
    html = re.sub(r'<nav.*?>', '', html, flags=re.DOTALL)
    html = re.sub(r'<button.*?>', '', html, flags=re.DOTALL)
    html = re.sub(r'<a.*?>', '', html, flags=re.DOTALL)

    clean_text=re.sub(r'<.*?>','',html)

    with codecs.open(result_file,'w','utf-8') as file:
        file.write(clean_text)
delete_html_tags('draft.html')
