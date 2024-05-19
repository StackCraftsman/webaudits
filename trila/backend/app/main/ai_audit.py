import anthropic
import base64

def ux_audit(image_path):
    # Open the image file and read its contents
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    client = anthropic.Anthropic(
        api_key = ""
    )

    with client.messages.stream(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        system="conduct a comprehensive UX audit for these screens and provide detailed analysis and recommendations on the following aspects:\n\n1. Copy:\n   - Evaluate the clarity, conciseness, and tone of the content throughout the website/app.\n   - Assess the readability and accessibility of the copy for users with varying levels of literacy and language proficiency.\n   - Identify areas where the copy could be improved to enhance user understanding and engagement.\n\n2. Accessibility:\n   - Analyze the website/app's compliance with accessibility standards (WCAG, Section 508, etc.).\n   - Check for proper implementation of alternative text for images, color contrast ratios, keyboard navigation, and screen reader compatibility.\n   - Identify any potential barriers or challenges for users with disabilities and provide recommendations for improvements.\n\n3. Visibility of System Status:\n   - Evaluate the presence and effectiveness of system status indicators, such as loading spinners, progress bars, and error messages.\n   - Ensure that users receive clear and timely feedback on the current state of the system and any ongoing processes.\n   - Suggest enhancements to improve the visibility and comprehensibility of system status information.\n\n4. Recognition Rather Than Recall:\n   - Assess the website/app's ability to minimize the user's memory load by providing clear and intuitive cues, instructions, and prompts.\n   - Identify areas where users may be required to recall information from one part of the interface to another, and recommend solutions for better recognition.\n   - Evaluate the effectiveness of help documentation, tooltips, and contextual guidance in supporting user recognition.\n\n5. Page Layout:\n   - Analyze the overall layout and organization of content on each page or screen.\n   - Evaluate the hierarchy, grouping, and alignment of elements for optimal visual flow and scanability.\n   - Identify areas where the layout could be improved to enhance readability, reduce clutter, and improve the overall user experience.\n\n6. User Control and Freedom:\n   - Assess the level of control and freedom provided to users for navigating and interacting with the website/app.\n   - Evaluate the availability and clarity of options for undoing actions, canceling processes, or exiting unwanted states.\n   - Identify areas where users may feel trapped or unable to control their experience, and provide recommendations for improving user agency.\n\n7. Consistency:\n   - Evaluate the consistency of design patterns, terminology, and interactions across the website/app.\n   - Identify any inconsistencies or deviations from established standards or guidelines.\n   - Recommend improvements to ensure a cohesive and predictable user experience throughout the website/app.\n\n8. Overall User Experience:\n   - Provide an overall assessment of the website/app's user experience, considering factors such as ease of use, visual design, efficiency, learnability, and satisfaction.\n   - Identify any significant pain points, frustrations, or areas of confusion that may negatively impact the user experience.\n   - Suggest comprehensive improvements or redesigns to enhance the overall user experience and meet user needs and expectations.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": encoded_image
                        }
                    },
                    {
                        "type": "text",
                        "text": "do my audit"
                    }
                ]
            }
        ]
    ) as stream:
        for text in stream.text_stream:
            yield text


