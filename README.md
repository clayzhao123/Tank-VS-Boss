# Tank-VS-Boss
In order to concretely study the coding capabilities of the current top AI, I tried to use Claude 3.5 sonnet to complete a bullet-hell shooting game. I will come up with the idea of ​​the content of this shooting game, and AI will be responsible for the code implementation, so as to test whether the current AI coding capabilities can help humans complete some small projects.
At present, this game is not finished. Due to the limited computing power of Claude 3.5 sonnet I have, it will be continuously updated in the future.


为了具象化地研究目前的顶级AI的代码能力，我尝试用Claude 3.5 sonnet完成一个弹幕射击游戏，这个射击游戏的内容的想法将有我来提出，而AI负责代码实现，以此来测试目前的AI的代码能力是否可以帮助人类完成一些小型项目。
目前这个游戏并没有做完，由于我掌握的Claude 3.5 sonnet算力有限，未来将不断更新。

I will put the prompt text for Claude below, and also synchronize some situations and instructions. Thank you.

之后我将会把每次给Claude的提示文本放到下面，也会同步一些情况和说明，谢谢。


1.（First prompt text）

I want to make a bullet-hell game. The idea is:
1. There is a protagonist who fires straight bullets
2. There is a boss who fires all kinds of bullets
3. The protagonist and the boss will lose health when they touch each other's bullets
Please generate

我想做一个弹幕游戏，设想大概是：
1. 有一个主角，主角会发射直线的弹幕
2.有一个boss，boss会发射各种各样的弹幕
3.主角和boss碰到对方的弹幕都会扣血
请你生成

2.
How can I run this program

我该怎么运行这段程序

3.
I hope to make some changes and improvements to the game. Please change the code accordingly to meet my needs:
1. I hope the protagonist is a tank. It can fire vertical bullets at a rate of 5 per second. Each bullet can make the boss lose 10 drops of blood. It can only move by keyboard "WASD". The blood volume is 100.
2. I hope the boss's blood volume is 1000. The boss can only move horizontally at the top of the game interface. The direction and size of movement are random.
3. If the tank dies, I hope there will be a settlement animation to count the game time and how much blood volume the boss has attacked. If the boss is defeated, I hope there will also be a settlement animation, such as the word "win!"

我希望对游戏做一些修改和提升，请你相应地改动代码以符合我的需求：
1.我希望主角是一个坦克，它可以发射竖直方向的子弹，射速是每秒5发，每发可让boss掉10滴血。它只能依靠键盘“WASD”来移动，血量是100.
2.我希望boss的血量是1000，boss只能在游戏界面的顶部横向移动，移动的方向和大小随机。
3.如果坦克死了，我希望有一个结算动画，统计游戏时长、攻击了boss多少血量，如果打赢了boss，我希望也有一个结算动画，比如“win！”的字样。

4.
I want to make some changes and improvements to the game. Please modify the code accordingly to meet my needs:
1. I hope to be able to add a texture effect to the boss and tank by importing pictures, that is, just attach a texture to the tank and boss. If this operation cannot be achieved, please let me know.
2. I hope to fix the bug that the bullets fired by the tank are invisible
3. I hope to have the possibility to change the background of the game. The background of the game can be modified by importing pictures. If this operation cannot be achieved, please let me know.

我希望对游戏做一些修改和提升，请你相应地改动代码以符合我的需求：
1.我希望可以让我通过图片导入的方式给boss和坦克添加一个贴图效果，也就是只是在坦克和boss上附加一个贴图，如果这个操作不能实现，请告知我。
2.我希望修复坦克发射的子弹看不见的bug
3.我希望有更改游戏背景的可能，通过导入图片可以修改游戏的背景。如果这个操作不能实现，请告知我。

5.
Does the tank need to press a button to fire bullets? Why is there still no bullets after I run it?

坦克发射子弹需要按键吗，为什么我运行之后还是没有子弹呢？

6.
I hope to make some changes and improvements to the game. Please change the code accordingly to meet my needs:
1. I hope the game frame rate can be higher. The current displacement of the tank gives people a feeling of not being smooth.
2. I hope to add a setting: when the tank hits the boss and the damage reaches 500, you can press the right mouse button to release the "big move". The "big move" is an energy ball that is 2-3 times larger than the tank character model. After releasing this energy ball, the energy ball will maintain a certain speed and move vertically upward. If it hits the boss, it will explode and cause 200 HP damage to the boss.
3. I hope that the boss's attacks will be more intensive and more regular. You can refer to the fan-made bullet game of [Touhou Project]
4. I hope that no matter whether the tank dies or the boss dies, the settlement screen will always be maintained, and in the settlement screen, give two options: a) "Restart", that is, click to restart the game b) "Exit", that is, click to close the game.



我希望对游戏做一些修改和提升，请你相应地改动代码以符合我的需求：
1.我希望游戏帧率能高一点，目前坦克的位移给人一种不太流畅的感觉
2.我希望增加一个设定：当坦克击中boss伤害累计达到500时，可以按鼠标右键释放“大招”，“大招”是一个比坦克人物模型大2-3倍的能量球，释放这个能量球之后，能量球会保持一定速度竖直向上运动，如果碰到boss，则会爆炸，会造成对boss200血量的伤害。
3.我希望boss的攻击更加密集，更加有规律性，可以参考 【东方Project】 的同人弹幕游戏
4.我希望不论坦克死亡还是boss死亡，结算画面一直保持，并且在结算画面中，给与两个选项：a)"重新开始"，即点击后重新开始游戏 b)"退出"，即点击后关闭游戏。

7.
I hope to make some changes and improvements to the game. Please change the code accordingly to meet my needs:
1. Double-clicking the spacebar can "clear the screen", that is, all bullets fired by the boss at that time can be instantly cleared. The tank has 3 chances to clear the screen, and I hope that the number of screen clears currently available can be displayed in real time on the game UI.
2. I hope that after the boss causes 20 damage to the tank, it will release a "special skill", which is a laser that lasts for 2 seconds in the vertical direction. If the tank is hit by the laser, it will suffer 15 health damage per second.
3. I hope that a start interface will be displayed at the beginning of the game. Only after clicking the start icon, the game will really start.


我希望对游戏做一些修改和提升，请你相应地改动代码以符合我的需求：
1.双击空格可以“清屏”，也就是可以瞬间清除当时boss发射的所有子弹。坦克有3次清屏机会，并且我希望在游戏UI上可以实时展示目前可用的清屏次数。
2.我希望boss在对坦克造成伤害达到20之后，释放一个“特殊技能”，是一个沿着竖直方向持续2秒的激光，如果坦克被激光击中，那么每秒将受到15血量的伤害。
3.我希望游戏开始时会显示一个开始的界面，只有点击开始的图标之后，游戏才会真正开始。


