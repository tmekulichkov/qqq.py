english = {}
def main():   #этот код для изучения английских слов(или повторения)
    intro()
    global english
    application(english)   # приложение, применение, заявка, заявление.
    post(english)          # пост, должность, после, почта.
    task(english)          # задача, задание.
    background(english)    # фон, предпосылка, фоновый режим.
    equipment(english)     # оборудование, оснащение.
    tool(english)          # инструмент, орудие.
    maintain(english)      # поддерживать, сохранять, утверждать.
    drawback(english)      #недостаток, препятствие.
    gadget(english)        #приспособление, устройство.
    '''look_around(english)   #осматривать.
    reach_out_to(english)  #постучаться в личку.
    live_reload(english)   #автоматическое обновление страницы.'''
    bye(english)
    print(english)
    goodbye()

def intro():
    print('это программа для повторения или изучения английских слов;')
    print(english)

def application(english):
    translate = str(input('приложение,применение,заявка,заявление: '))
    if translate.lower() == 'application':
        print('совершенно правильно!\n')
    else:
        while (translate.lower() != 'application') and (translate.lower() != 'help'):
            print(F'вы совершили ошибку in: [{translate}]')
            translate = str(input('попробуйте еще раз, или напишите: \'help\' если не знаете! '))
            if translate.lower() == 'application':
                print('правильно\n')
            elif translate.lower() == 'help':
                print('правильный ответ : \'application\'!') 
            else:
                print('введите правильное значение!')
                continue
    english['приложение,применение,заявка,заявление'] = translate
    print('you was learning:\n', english['приложение,применение,заявка,заявление'])
    print('\f')
        
def post(english):
    post = str(input('пост, должность, поста, после: '))
    if post.lower() == 'post':
        print('правильный ответ!\n')
    else:
        while (post.lower() != 'post') and (post.lower() != 'help'):
            print(f'вы имели в виду: {post}? Это совершенно неправильно! ')
            post = str(input('попробуйте еще раз,или введите : \'help\' если не знаете! '))
            if post.lower() == 'post':
                print('совершенно правильный ответ!')
            elif post.lower() == 'help':
                print('правильный ответ : \'post\'!')
            else:
                print('введите правильное значение!\n')
                continue
    english['пост,должность,почта,после'] = post
    print('you only was learning:', english['пост,должность,почта,после'])
    
def task(english):
    task = str(input('задача, задание: '))
    if task.lower() == 'task':
        print('вы совершенны!\n')
    else:
        while (task.lower() != 'task') and (task.lower() != 'help'):
            print(f'{task} - это неправильный перевод')
            task = str(input('введите снова перевод: (или \'help\') - если не знаете!\n'))
            if task.lower() == 'task':
                print('это правильно!\n')
            elif task.lower() == 'help':
                print('правильный ответ : \'task\'!\n')
            else:
                print('введите правильное значение!\n')
                continue
    english['задание,задача'] = task
    print('you was learning:\n', english['задание,задача'])
    print('\f')
    
def background(english):
    background = str(input('фон,предпосылка,фоновый режим: '))
    if background.lower() =='background':
        print('отлично!\n')
    else:
        while (background.lower() != 'background') and (background.lower() != 'help'):
            print(f'{background} - ошибка! повторите еще раз(или \'help\') - если не знаете!' )
            background = str(input('введите перевод: '))
            if background.lower() == 'background':
                print('великолепно!')
            elif background.lower() == 'help':
                print('правильный ответ : \'background\'!')
            else:
                print('введите правильное значение!\n')
                continue
    english['фон,предпосылка,фоновый режим'] = background
    print('you was learning:\n', english['фон,предпосылка,фоновый режим'])
    print('\f')
def equipment(english):
    equipment = str(input('оборудование, оснащение '))
    if equipment.lower() == 'equipment':
        print('правильный ответ!\n')
    else:
        while (equipment.lower() != 'equipment') and (equipment.lower() != 'help'):
            print(f'{equipment.capitalize()}  - тут была где-то допущена ошибка!')
            equipment = str(input('(\'help\') - и вы получите перевод! Или же введите перевод слова! '))
            if equipment.lower() == 'equipment':
                print('Правильно!\n')
            elif equipment.lower() == 'help':
                print('правильный ответ : \'equipment\'!')
            else:
                print('вы вышли за предела ответov!')
                continue
    english['оборудование,оснащение'] = equipment
    print('you was learning:\n', english['оборудование,оснащение']) 
    print('\f')

def tool(english):
    tool = str(input('инструмент, орудие: '))
    if tool.lower() == 'tool':
        print('это прекрасный ответ!)')
    else:
        while (tool.lower() != 'tool') and (tool.lower() != 'help'):
            print(F'{tool} - увы, но это неправильно')
            tool = str(input('повторите попытку, или напишите \'help\' - это даст вам ответ: '))
            if tool.lower() == 'tool':
                print('замечательно!')
            elif tool.lower() == 'help':
                print('правильный ответ : \'tool\'!')
            else:
                print('вы вышли за грань программы')
                continue
    english['инструмент, орудие'] = tool
    print('you was learning:\n', english['инструмент, орудие'])
def maintain(english):
    translate = str(input('поддерживать, сохранять, утверждать: '))
    if translate.lower() == 'maintain':
        print(f'совершенно правильно!')
    else:
        while (translate.lower() != 'maintain') and (translate.lower() != 'help'):
            translate = str(input(f'{translate} - неверно!\
                    желаете повторить попытку \
                    ( или если НЕзнаете - \'help\') - will be a show a qustion: '))
            if translate.lower() == 'maintain':
                print(f'совершенно правильно! ')
            elif translate.lower() == 'help':
                print(f'правильный ответ: \'maintain\'.')
            else:
                print('вы вышли за пределы допустимых ответов!')
                continue
    english['поддерживать, сохранять, утверждать'] = 'maintain'
    print(f'вы выучили только что новое слово: ', english['поддерживать, сохранять, утверждать'])
    print('\n')
def drawback(english):
    drawbacking = str(input('недостаток, препятствие: '))   #недостаток, препятствие.
    if drawbacking.lower() == 'drawback':
        print('совершенный правильный ответ!')
    else:
        while (drawbacking.lower() != 'drawback') and (drawbacking.lower() != 'help'):
            print(f'\'{drawbacking}\'-неправильный ответик!если не знаете ответ: \'help\'.')
            drawbacking = str(input('недостаток, препятствие: '))
            if drawbacking.lower() == 'drawback':
                print('правильный ответ!')
            elif drawbacking.lower() == 'help':
                print(f'правильный ответик: \'drawback\'.')
            else:
                print('вы вышли за грань моей программы>!')
                continue
    english['недостаток, препятствие'] = 'drawback'
    print(f'you was leaning a ', english['недостаток, препятствие'], end='.')

def gadget(english):
    gadgeting = str(input('приспособление, устройство: '))    #приспособление, устройство.
    if gadgeting.lower() == 'gadget':
        print('прыовальный ответъ!\n')
    elif gadgeting.lower() != 'gadget':
        while (gadgeting.lower() != 'gadget') and (gadgeting.lower() != 'help'):
            print(f'\'{gadgeting}\'-увы, но, нет!(если не знаете) - \'help\'.')
            gadgeting = str(input('приспособление, устройство: '))
            if gadgeting.lower() == 'gadget':
                print(f'пьюти фЬЮЫЫЫЫЫЫЫЫ,правильно...')
                
def bye(english):
    print(f'вы выучили:')
    total = english
    return total
def goodbye():
    print('and at the moment come time for end the program')
    a = input('press enter to exit')
main()

  #change me

