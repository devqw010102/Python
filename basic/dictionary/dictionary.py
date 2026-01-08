# import dictionary
ice = {'메로나' : 1000, '폴라포' : 1200, '빵빠레' : 1800 }

print(ice)
print(ice['메로나'])
# print(ice.keys())
# print(ice.values())
# print(ice.items())

# put dictionary
ice['죠스바'] = 1200
ice['월드콘'] = 1500
print(ice)

inventory = { '메로나' : [300, 20],
              '비비빅' : [400, 3],
              '죠스바' : [250,100]
            }

print(inventory['메로나'][0])
