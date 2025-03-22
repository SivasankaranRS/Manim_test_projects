from manim import *

class Integral_question_1(Scene):
    def construct(self):
        self.play_title()
        self.solution_integral_1()
        self.solution_integral_2()
        
    def show_Text(self, text, font_size, display_time):
        new_text = Text(text, font_size=font_size)
        self.play(Write(new_text))
        self.wait(display_time)
        self.play(FadeOut(new_text))
        self.wait(0.5)
        
    def show_math(self, mobject, display_time,case):
        self.play(Write(mobject))
        self.wait(display_time)
        
        match (case):
            case 1:
                self.play(FadeOut(mobject))
                self.wait(0.5)
            case 2:
                self.wait(0.5)               

        
    def play_title(self):
        title = Tex("Evalute the integral",font_size = 48)
        self.play(Write(title))
        self.wait(0.5)
        
        self.play(title.animate.shift(UP * 2))
        self.wait(0.5)
        question = MathTex(r"\int_{0}^{1}\bigg\{\frac{1}{x}\bigg\}dx")
        self.show_math(question,display_time = 1, case = 2)
        self.play(FadeOut(question))
        self.play(FadeOut(title))
        

    
    def solution_integral_1(self):
        question = MathTex(r"\int_{0}^{1}\bigg\{\frac{1}{x}\bigg\}dx")
        text_1 = Tex(r"Substitute")
        math_text_1 = MathTex(r"\frac{1}{x} = u \to x = \frac{1}{u}\to dx = \frac{-1}{u^2 }du ")
        text_2 = Tex(r"\text{New limits: } $0 \to \infty,\quad 1 \to 1$")
        math_text_2 = MathTex(r"\int_{\infty}^{1}\{u\}\times\frac{-1}{u^2}du")
        text_3 = Tex(r"\text{Since $u$ is a dummy variable, replace it with } $x$.")
        math_text_3 = MathTex(r"\int_{\infty}^{1}\{x\}\times\frac{-1}{x^2}dx")
        math_text_4 = MathTex(r"\int_{\infty}^{1}-\frac{\{x\}}{x^2} dx")
        text_4 = Tex(r"\text{Now we change the limits of the integrand}")
        math_text_5 = MathTex(r"\int_{1}^{\infty}\frac{\{x\}}{x^2} dx")
        text_5 = Tex(r"\text{We can write }$\{x\}$ \text{ as } $x-[x]$ ")
        text_6 = Tex(r"\text{Where }$[x]$\text{ is the greatest integer function.}")
        text_7 = Tex(r"\parbox{7cm}{\centering This is an indefinite integral. Therefore we can take a limit $t$ as $t \to \infty$}")

        text_8 = Tex(r"\text{Let's solve the second Integral}")
        math_text_6 = MathTex(r"\lim_{t\to\infty} \bigg(\ln(t)\bigg)- \lim_{t\to\infty}\underbrace{ \int_{1}^{t}\frac{[x]}{x^2} }_{I_{1} }dx")
        
        math_list_1 = [
            r"\int_{1}^{\infty}\frac{x-[x]}{x^2} dx",
            r"\int_{1}^{\infty}\frac{x}{x^2} - \frac{[x]}{x^2}dx",
            r"\int_{1}^{\infty}\frac{1}{x}dx - \int_{1}^{\infty}\frac{[x]}{x^2}dx"
        ]
        
        math_list_2 = [
            r"\lim_{t\to\infty}\Biggr(\int_{1}^{t}\frac{1}{x}dx - \int_{1}^{t}\frac{[x]}{x^2}dx\Biggr)",
            r"\lim_{t\to\infty}\int_{1}^{t}\frac{1}{x}dx - \lim_{t\to\infty}\int_{1}^{t}\frac{[x]}{x^2}dx",
            r"\lim_{t\to\infty} \bigg(\ln(x)\bigg|_{1}^{t}\bigg)- \lim_{t\to\infty}\int_{1}^{t}\frac{[x]}{x^2}dx",
            r"\lim_{t\to\infty} \bigg(\ln(t)-\ln(1)\bigg)- \lim_{t\to\infty}\int_{1}^{t}\frac{[x]}{x^2}dx",
            r"\lim_{t\to\infty} \bigg(\ln(t)\bigg)- \lim_{t\to\infty}\int_{1}^{t}\frac{[x]}{x^2}dx",
        ]
        
        self.show_math(question,display_time = 1, case = 2)
        self.play(question.animate.to_edge(UP))
        self.wait(0.5)
        
        self.show_math(text_1, display_time = 0.5, case = 2)
        self.play(text_1.animate.shift(UP * 1.5))
        
        self.show_math(math_text_1, display_time = 1, case = 2)
        
        self.play(Write(text_2.shift(DOWN * 2)))
        
        self.play(FadeOut(text_1))
        
        self.play(math_text_1.animate.shift(UP * 1.5))
        
        self.play(FadeOut(question))
        self.play(FadeIn(question.move_to(ORIGIN)))
        self.wait(1)
        
        self.play(TransformMatchingTex(question,math_text_2))
        self.wait(0.5)
        
        self.play(FadeOut(math_text_1,text_2))
        
        self.play(Write(text_3.shift(UP * 2)))
        self.wait(0.5)
        self.play(TransformMatchingTex(math_text_2, math_text_3))
        self.play(FadeOut(text_3))
        self.wait(0.5)        
        self.play(TransformMatchingTex(math_text_3, math_text_4))
        self.wait(0.5)
        
        self.play(Write(text_4.shift(UP * 2)))
        self.wait(0.5)
        self.play(TransformMatchingTex(math_text_4, math_text_5))
        self.wait(0.5)
        self.play(FadeOut(text_4))
        self.wait(0.5)
        self.play(FadeIn(text_5.shift(UP * 2)))
        self.play(FadeIn(text_6.shift(DOWN * 2)))
        self.wait(0.5)
        
        temp_Math_text_1 = MathTex(math_list_1[0])
        self.play(TransformMatchingTex(math_text_5,temp_Math_text_1))
        self.wait(0.3)
        self.play(FadeOut(text_5,text_6))
        self.wait(0.3)
        self.play(FadeOut(temp_Math_text_1))
        
        current_formula = None
        for step in math_list_1:
            next_formula = MathTex(step)
            if current_formula is None:
                self.play(Write(next_formula))
            else:
                self.play(TransformMatchingTex(current_formula, next_formula),duration = 0.5)
                self.remove(current_formula)
            current_formula = next_formula
            self.wait(3)
        
        self.play(Write(text_7.shift(UP * 2)))
        
        self.play(FadeOut(current_formula))
        self.play(FadeOut(text_7))
        self.wait(0.1)
        
        current_formula = None
        for step in math_list_2:
            next_formula = MathTex(step)
            if current_formula is None:
                self.play(Write(next_formula))
            else:
                self.play(TransformMatchingTex(current_formula, next_formula),duration =1)
                self.remove(current_formula)
            current_formula = next_formula
            self.wait(3)
            
        self.play(Write(text_8.shift(UP * 2)))
        self.play(TransformMatchingTex(current_formula, math_text_6))
        self.wait(0.1)
        self.play(FadeOut(text_8,math_text_6))
        self.wait(0.5)
        
    def solution_integral_2(self):
        math_text_1 = MathTex(r"I_{1}=\int_{1}^{t}\frac{[x]}{x^2}dx")
        text_1 = Tex(r"We can write the split the integral like this")
        math_text_2=MathTex(r"I_{1}=\int_{1}^{2}\frac{[x]}{x^2}dx+\int_{2}^{3}\frac{[x]}{x^2}dx+\int_{3}^{4}\frac{[x]}{x^2}dx+\dots+\int_{t-1}^{t}\frac{[x]}{x^2}dx")
        text_2 = Tex(r"\parbox{7cm}{\centering Because the greatest  integer fuction we can write the resultend integral as this}")
        math_text_3 = MathTex(r"I_{1}=\int_{1}^{2}\frac{1}{x^2}dx+\int_{2}^{3}\frac{2}{x^2}dx+\int_{3}^{4}\frac{3}{x^2}dx+\dots+\int_{t-1}^{t}\frac{t-1}{x^2}dx").scale(0.8)
        math_text_4 = MathTex(r"I_{1}=\int_{1}^{2}\frac{1}{x^2}dx+2\int_{2}^{3}\frac{1}{x^2}dx+3\int_{3}^{4}\frac{1}{x^2}dx+\dots+(t-1)\int_{t-1}^{t}\frac{1}{x^2}dx").scale(0.8)
        text_3 = Tex(r"\text{To simplify further, we can express it as a summation:}")
        math_text_5 = MathTex(r"I_{1}(t)=\sum_{i=2}^{t}\bigg((i-1)\int_{i-1}^{i}\frac{1}{x^2}dx\bigg)")
        text_4 = Tex(r"Now, substitute $i=u+1$, so that $u$ runs from $1$ to $t-1$.")
        
        math_list_1 = [
            r"I_{1}=\sum_{u=1}^{t-1}\bigg((u)\int_{u}^{u+1}\frac{1}{x^2}dx\bigg)",
            r"I_{1}=\sum_{u=1}^{t-1}u\bigg(- \frac{1}{x}\bigg|_{u}^{u+1}\bigg)",
            r"I_{1}=\sum_{u=1}^{t-1}-u\bigg(\frac{1}{u+1}- \frac{1}{u}\bigg)",
            r"I_{1}=\sum_{u=1}^{t-1}-u\bigg(\frac{u-(u+1)}{u(u+1)}\bigg)",
            r"I_{1}=\sum_{u=1}^{t-1}\frac{1}{(u+1)}"
        ]
        
        text_s_1 = Tex(r"\text{Let's substitute further:}")
        math_text_s_1 = MathTex(r"\lim_{t\to\infty} \bigg(\ln(t)\bigg)- \lim_{t\to\infty}\sum_{u=1}^{t-1}\frac{1}{(u+1)}")
        math_text_s_2 = MathTex(r"\lim_{t\to\infty} \bigg(\ln(t)-\sum_{u=1}^{t-1}\frac{1}{(u+1)}\bigg)")
        
        text_5 = Tex(r"\text{Since the limits tends to infinity }t-1\text{ be changed to }t .")
        math_text_6 = MathTex(r"\lim_{t\to\infty} \bigg(\ln(t)-\sum_{u=1}^{t}\frac{1}{(u+1)}\bigg)")
        text_6 = Tex(r"\parbox{7cm}{\centering This is a similar to very famous contant called the Euler-Mascheroni constant}")
        math_text_7 = MathTex(r"\gamma = \lim_{ n \to \infty }\bigg(-\ln n + \sum_{k=1}^{n} \frac{1}{k} \bigg) ")
        math_text_8 = MathTex(r"-\gamma = -\Biggr( \lim_{ n \to \infty }\bigg(-\ln n + \sum_{k=1}^{n} \frac{1}{k} \bigg) \Biggr)")
        math_text_9 = MathTex(r"-\gamma = \lim_{ n \to \infty }\bigg(\ln n - \sum_{k=1}^{n} \frac{1}{k} \bigg)")
        
        text_7 = MathTex(r"\text{Now lets substitute }k = u+1")
        
        math_list_2 =[
            r"-\gamma = \lim_{ n \to \infty }\bigg(\ln n - \sum_{u=0}^{n} \frac{1}{u+1} \bigg)",
            r"-\gamma = \lim_{ n \to \infty }\bigg(\ln n - \sum_{u=1}^{n} \frac{1}{u+1} -1\bigg)",
            r"-\gamma + 1= \lim_{ n \to \infty }\bigg(\ln n - \sum_{u=1}^{n} \frac{1}{u+1} \bigg)",
            r"\int_{0}^{1}\bigg\{\frac{1}{x}\bigg\}dx = \lim_{t\to\infty} \bigg(\ln(t)-\sum_{u=1}^{t}\frac{1}{(u+1)}\bigg)= -\gamma+1",
            r"\therefore \int_{0}^{1}\bigg\{\frac{1}{x}\bigg\}dx=-\gamma +1"
        ]
        
        self.play(Write(math_text_1))
        self.play(FadeIn(text_1.shift(UP * 2)))
        self.wait(0.5)
        self.play(TransformMatchingTex(math_text_1,math_text_2))
        self.play(FadeOut(text_1))
        self.play(FadeIn(text_2.shift(UP * 2)))
        self.wait(0.5)
        self.play(TransformMatchingTex(math_text_2,math_text_3))
        self.play(FadeOut(text_2))
        self.play(TransformMatchingTex(math_text_3,math_text_4))
        self.play(FadeIn(text_3.shift(UP * 2)))
        self.play(FadeIn(text_4.shift( DOWN * 2)))
        self.wait(0.5)
        self.play(TransformMatchingTex(math_text_4,math_text_5))
        self.play(FadeOut(text_3,text_4))
        self.wait(0.5)
        self.play(FadeOut(math_text_5))
        
        current_formula = None
        for step in math_list_1:
            next_formula = MathTex(step)
            if current_formula is None:
                self.play(Write(next_formula))
            else:
                self.play(TransformMatchingTex(current_formula, next_formula),duration =1)
                self.remove(current_formula)
            current_formula = next_formula
            self.wait(1)
        
        self.play(FadeOut(current_formula))
        self.wait(0.5)
        self.play(Write(text_s_1))
        self.wait(0.5)
        self.play(text_s_1.animate.shift (UP * 2))
        self.play(FadeIn(math_text_s_1))
        self.play(TransformMatchingTex(math_text_s_1,math_text_s_2))
        self.play(FadeOut(text_s_1))
        self.wait(0.5)
        self.play(FadeIn(text_5.shift(UP * 2)))
        self.wait(0.3)
        self.play(TransformMatchingTex(math_text_s_2,math_text_6))
        self.wait(0.5)
        self.play(FadeOut(math_text_6,text_5))
        self.play(Write(text_6))
        self.play(text_6.animate.shift(UP * 2))
        self.wait(0.3)
        
        self.play(FadeIn(math_text_7))
        self.wait(0.5)
        self.play(FadeOut(text_6))
        
        self.play(FadeIn(text_7.shift( UP * 2)))
        
        self.play(TransformMatchingTex(math_text_7,math_text_8))
        self.play(FadeOut(text_7))
        self.wait(0.3)
        self.play(TransformMatchingTex(math_text_8,math_text_9))
        self.wait(0.3)
        self.play(FadeOut(math_text_9))
        
        
        current_formula = None
        for step in math_list_2:
            next_formula = MathTex(step)
            if current_formula is None:
                self.play(Write(next_formula))
            else:
                self.play(TransformMatchingTex(current_formula, next_formula),duration =1)
                self.remove(current_formula)
            current_formula = next_formula
            self.wait(3)