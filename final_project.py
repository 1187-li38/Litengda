#coding:gbk
'''
���ߣ����ڴ�
Ŀ�ģ����ı������ϵ�����ȡ
2019/12/31
'''
string_connection=""
string_node=""
names={"�ɲ�","��Ҷ","������","԰��","�¹�","����","����","��Ҳ","���","����","��ɫ����","����","�����","���¾���"}#�������ֵ��ֵ�
for name1 in names:
    for name2 in names:#��������֮���ϵ
        times = 0
        passage=open("�����Ľֵ�.txt",'r',encoding='gbk')
        for x in passage.readlines():
            if (set(list(name1)) < set(list(x))) and (set(list(name2)) < set(list(x))):#�ж������Ƿ��Ƕ�����Ӽ�
                times += 1
        if name1==name2 and times!=0:
          string=("%s %s %s\n"%(name1,name2,times))
          string_node += string
        elif name1!=name2 and times!=0:
            string = ("%s %s %s\n" % (name1, name2, times))
            string_connection += string
        passage.close()
print(string_connection,string_node)
file1=open("string_connection.txt","w",encoding="gbk")#д���ļ�
file1.write(string_connection)
file1.close()
file2=open("string_node.txt","w",encoding="gbk")
file2.write(string_node)
file2.close()
            G.add_weighted_edges_from([(line[0],line[1],int(line[2]))])
    nx.draw(G,pos=nx.shell_layout(G),node_size=1000,node_color = '#A0CBE2',edge_color='#A0CBE1',with_labels = True,font_size=12)
    plt.show()
