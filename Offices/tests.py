#
# data=(      {  "27":"AAA"},
#             {"34":"BBB"},
#             {"10":"CCC"},
#             {"70":"DDD"},
#             {"65":"EEE"},
#             {"90":"FFF"},
#             {"83":"GGG"},
#             {"120":"HHH"},
#             {"210":"III"},
#             {"330":"JJJ"},
#             {"111":"KKK"},
#             {"50":"LLL"},
#             {"56":"MMM"},
#             {"70":"NNN"},
#             {"85":"OOO"},
#             {"14":"PPP"},
#             {"25":"QQQ"},
#             {"98" : "RRR"},
#              {"160":"SSS"},
#             {"156":"TTT"},
#             {"34":"UUU"},
#             {"67":"VVV"},
#             {"96":"WWW"},
#             {"25":"XXX"},
#             {"36":"YYY"},
#             {"44":"ZZZ"})
#
# x = int(input("Please Enter an Integer Value : "))
# #####################STEP1###############################
# i=0
# match=''
# atched_words=''
# for dic in data:
#     for k,v in dic.items():
#         if x==int(k):
#             i+=1
#             match=match+v+"  "
# if i > 0:
#     print(str(i)+' exact matches found. '+match)
# else:
#     print("No Exact Match Found")
#
# #######################STEP2##########################
# val1=0
# val2=0
#
# li=[]
# exist=0
# for item in data:
#     for k,v in item.items():
#         if val1==int(k):
#             break
#         else:
#          val=x-int(k)
#          check=0
#          matched_words = ''
#          for item1 in data:
#             for k1, v1 in item1.items():
#                 if val==int(k1):
#                     val1 = val
#                     dic={v:v1}
#                     li.append(dic)
#                 if val2==int(k1):
#                     print(val2)
#                 if k == k1:
#                     pass
#                 else:
#                  val2 = val - int(k1)
#                  print(val2)
#                 # print(val2,k1)
#                 if check==0:
#                     matched_words = matched_words+" "+v + v1
#                     i+=1
#                 if val2==int(k1):
#                     print(val2)
#                  # print('okkk')
#                     if val2+int(k1)+int(k)==x:
#                      matched_words = matched_words +  k1
#                      print(matched_words)
#                      exist=1
# match=''
#
# if li:
#     length=li.__len__()
#     for val in li:
#         for k,v in val.items():
#             match=match+"( "+str(k)+" , "+str(v)+" ) "
#     print(str(length)+' compound '+str(length)+" match found "+match)
# else:
#     print('No Compound Match Found')
#
# if exist==1:
#     print(matched_words)
# else:
#     print('triple matched words not found')

data="how,,,r,,,u,,,"
print(data.split(',,,'))