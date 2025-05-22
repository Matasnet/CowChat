import cowsay
import html

def generate_cowsay(name, text, color):
    msg = cowsay.get_output_string("cow", f"{name} mówi:\n{text}")
    msg = html.escape(msg)  # unikaj HTML injection

    lines = msg.split('\n')
    colored_lines = [f'<span style="color: {color}">{line}</span>' for line in lines]
    return "<br>".join(colored_lines)
