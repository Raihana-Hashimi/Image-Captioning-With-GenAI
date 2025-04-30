import gradio as gr

def greet(name, lname, intensity):
    return "Hello " + name + lname + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "text", "slider"],
    outputs=["text"]
)

demo.launch(server_name="127.0.0.1", server_port=7860)