alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
#括号的规则只有这一种


print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)


#开始有趣的了
speeds=['fast','medium','slow']
alien={
'x_position':0,
'y_position':25,
'speed':''
}
import random
#如果想使用random必须写这一行
alien['speed']=speeds.pop(random.randint(0,2))
print(alien['speed'])
while alien['x_position'] <=30:
	if alien['speed']=='slow':
		x_increasement=1
	elif alien['speed']=='fast':
		x_increasement=6
	elif alien['speed']=='medium':
		x_increasement=3
	alien['x_position']=alien['x_position']+ x_increasement
print(f"new x_position is {alien['x_position']}")