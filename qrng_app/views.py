from django.shortcuts import render
from django.template.loader import select_template
from django.conf import settings
import os

def qrng_page(request):
    template = select_template(['qrng.html'])

    if request.method == 'POST':
        # If the form is submitted, get the desired length from POST data
        desired_length = int(request.POST.get('desired_length', 10))
    else:
        # Default desired length if the form is not submitted
        desired_length = 0

    # Read the random bits from the text file
    file_path = os.path.join(settings.BASE_DIR, 'random_string.txt')
    with open(file_path, 'r') as file:
        content = file.read().strip()

    # Parse the content as a list of integers
    random_bits = [int(bit) for bit in content.strip('[]').split(',')]

    # Calculate the middle index
    middle_index = len(random_bits) // 2

    # Adjust the start and end indices based on the desired length
    start_index = middle_index - (desired_length // 2)
    end_index = middle_index + (desired_length // 2)

    # Get the selected bits
    selected_bits = random_bits[start_index:end_index]

    # Prepare the context data to pass to the template
    context = {
        'heading': 'QRNG based on noise from NISQ quantum device',
        'bits_count': desired_length,
        'random_bits': selected_bits,
    }

    return render(request, 'qrng.html', context)

