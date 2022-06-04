
import streamlit as st


def main():
    st.title('SITE PALPITES PARA APOSTAS ESPORTIVA')
    '''_____________________________________________'''
    st.success('Venha conferir nosso novo App para análise de jogos de futebol, para mercado de cantos e gol. ⬇️'
               'SÓ AQUI VOCÊ É GREEN! ACESSO DO LINK ABAIXO  ⬇️')
    L_imagem = 'https://i.postimg.cc/bvSWpw7S/HELISI-Bet-Bot.png'
    L_site = 'https://bit.ly/3t24BpR'



    '''___Link com imagens _________________________________________________'''
    st.markdown(
        f'''<h3> CLIQUE AQUI ---> <a href="{L_site}"><img src="{L_imagem}" 
        width="800" height="400" "></h3>''', unsafe_allow_html=True)


    '''__Passado como um letreiro ___________________________________________'''
    st.markdown(
        f'''<h3><MARQUEE BEHAVIOR="alternate" DIRECTION="RIGHT" scrollamount="10" BGCOLOR="BLACK" WIDTH=100% >
         <a href="{L_site}"><img src="{L_imagem}" width="300" height="270" "></MARQUEE></h3>''',
        unsafe_allow_html=True)


    '''___Pulando igual doido rsss __________________________________________'''
    st.markdown(f'''
    <marquee direction="down" width="1000" height="500" behavior="alternate" style="border:solid" scrollamount= "20">
    <marquee behavior="alternate"><a href="{L_site}"><img src="{L_imagem}" width="500" height="300" ">''',
     unsafe_allow_html=True)


if __name__ == '__main__':
    st.set_page_config(page_title='IMAGE LINK',layout='wide')
    main()

#Tchau brigadu!!
