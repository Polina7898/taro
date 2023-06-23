import streamlit as st
import datetime
import prompt
import generator



st.title("""У таролога :red[Полины]""")
st.image('IMG_0611.PNG')
option = st.selectbox(
    'Каким методом разложить карты таро?',
    ('Кельтский Крест', 'Крест', 'Безмятежность дней'))

col1, col2 = st.columns(2)

with col1:
    name = col1.text_input('Введите свое Имя')

with col2:
    max_value = datetime.datetime.now()
    min_value = max_value - datetime.timedelta(days=36500)
    birtday = col2.date_input('Когды вы родились?', min_value = min_value, max_value = max_value)

qs = ''

if option != 'Безмятежность дней':
    qs = st.text_input('Введите свой вопрос')

if birtday and name and option:
    btn_get_taro = st.button(label='Получить расклад', type='primary')

    if btn_get_taro:
        if option == 'Кельтский Крест':
            prompts = prompt.generate_prompt(name, birtday, qs)
        elif option == 'Крест':
            prompts = prompt.prompt_krest(name, birtday, qs)

        elif option == 'Безмятежность дней':
            prompts = prompt.prompt_The_serenity_of_days(name, birtday)

        with st.spinner('Делаю магический расклад, подождите'):
            z = st.image('gadalka.gif')
            answer = generator.get_answer(prompts)
        z.empty()
        st.divider()
        st.subheader('Вот что карты показали')
        st.write(answer)
