TEXT="""La historia de la ópera tiene una duración relativamente corta 
    dentro del contexto de la historia de la música en general apareció 
    en 1597, fecha en que se creó la primera ópera."""

ANCHO=30

text_list = TEXT.split()
total_len = len(text_list[0])
lens = []
indexs = set([-1])
for idx in range(1, len(text_list)-1): 
    total_len += len(text_list[idx]) + 1 
    if total_len <= ANCHO and (1 + total_len + len(text_list[idx+1])) > ANCHO: 
        indexs.add(idx) 
        lens.append(total_len) 
        total_len = -1
indexs.add(len(text_list))
indexs = sorted(list(indexs))

for i in range(0,len(indexs)-2): 
    num = indexs[i+1]-indexs[i]-1 
    spaces = ANCHO-lens[i] 
    if num == 0: 
        num=1 
    q, r = spaces // num, spaces % num 
    a_list, b_list = [" "*q]*num + [""], [" "]*(r+1) + [""]*(num-r) 
    spaces_list = [z+x+y for x,y,z in zip(a_list,b_list, text_list[indexs[i]+1: indexs[i+1]+1] )] 
    print(" ".join(spaces_list))
print(" ".join(text_list[indexs[i+1]+1:]))