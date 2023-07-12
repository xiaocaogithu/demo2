import  requests
url='https://epub2.doc110.com/kns8/Brief/GetGridTableHtml'
data={
'IsSearch': 'true',
'QueryJson': {"Platform":"","DBCode":"CFLS","KuaKuCode":"CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"铁相关","Operate":"%=","BlurType":""}],"ChildItems":[]}]},"CodeLang":"ch"},
'PageName': 'defaultresult',
'DBCode': 'CFLS',
'KuaKuCodes': 'CJFQ,CCND,CIPD,CDMD,BDZK,CISD,SNAD,CCJD,GXDB_SECTION,CJFN,CCVD',
'CurPage': 1,
'RecordsCntPerPage': 20,
'CurDisplayMode': 'listmode',
'CurrSortField': '',
'CurrSortFieldType': 'desc',
'IsSentenceSearch': 'false',
'Subject': '',
}
header={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Cookie':'AUTH_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjQ4NDIyMTM1NTE4NjEyIiwidXNlcl9pZCI6MTIyODA3NywiZW1haWwiOiIiLCJleHAiOjE2ODg5NzQ3ODV9.ZNOh1UIU_rWLh4qItSV3hWIPqy6Sg1IuUufsguGdrkU; knsLeftGroupSelectItem=1%3B2%3B; ASP.NET_SessionId=2gjnzaghxlfqb5byu0lpse31; Ecp_ClientId=1230710144000442347; SID_kns8=123104; dblang=ch',

}
response=requests.post(url,data=data,headers=header)
response.encoding='utf-8'
print(response.text)