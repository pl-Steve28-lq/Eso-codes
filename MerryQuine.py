I=__import__;        r=I('random'
   );a=open('.     /merryqui\
     ne.  py '   .replace(                       # MERRY
     ' ','')).readlines(                        #
      );m=max(map(len,         a));f=[*map  (lambda s     :s.ljust(m),map       (str.rstrip,a
     ))];m =  max( map(       len,f       ));     fl=[   1]            *m     ;re=[       -1]*m
for i in list (range(len(     f))):       #By      Ste                  ve      28!!
 for j in [*  range(m)]:re    [j]+=       fl[     j];      fl[j]=0if f[i]     [j]!=' 'else fl[
j];v=[0]*m;     ins=lambda     s,i,       c:s     [:i]   +c+          s[1                  +i:]
sn=[];s4=[' '    *m*1**1 for   i in     range     (len   (f))];Q=300#Merry     Christmas 2022 :D

e=exec;V=0;P='''while v[ p:=r.randint(0,m-1)]>len(f)-re[p]and 1:pass|sn.append([p,0]);s2 = s4[:]|for i in sn:
 if i[1]==len(f)-v[i[0]]-1:s4[i[1]]=ins(s4[i[1]],i[0],f[i[1]] [i[0]]);v[i[0]]+=1;del sn[sn.index(i)]
 q=min(i[0] + r.randint(-1,1),m-1)| if 0<=i[1]<len(f):s2[i[1]]=ins(s2[i[1]],max(0,q),'*');i[1] += 1\n'''\
.replace('|', '\n');C='''I('time') . sleep( 0.1);I('os') . system('cls')\nfor i in s2: print(i); ''';e('while Q<m'
'*len(f):e(P*3+C);Q+=3\ns2=f;e(C)\nwhile V<len(f):f[V]="".join([*map(lambda x:"#"if x!=" "else x,f[V])]);e(C);V+=1')

