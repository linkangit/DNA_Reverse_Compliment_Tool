#!/usr/bin/env python3
"""
DNA Reverse Complement Tool

This tool takes a DNA sequence and returns its reverse complement.
The reverse complement is found by:
1. Replacing each base with its complement (A↔T, G↔C)
2. Reversing the resulting sequence
"""

def get_reverse_complement(sequence):
    """
    Returns the reverse complement of a DNA sequence.
    
    Args:
        sequence (str): DNA sequence containing A, T, G, C (case insensitive)
        
    Returns:
        str: Reverse complement of the input sequence
        
    Raises:
        ValueError: If sequence contains invalid characters
    """
    # Define complement mapping
    complement_map = {
        'A': 'T', 'T': 'A',
        'G': 'C', 'C': 'G',
        'a': 't', 't': 'a',
        'g': 'c', 'c': 'g'
    }
    
    # Validate input sequence
    valid_chars = set('ATGCatgc')
    if not all(char in valid_chars for char in sequence):
        invalid_chars = set(sequence) - valid_chars
        raise ValueError(f"Invalid characters found in sequence: {invalid_chars}")
    
    # Get complement
    complement = ''.join(complement_map[base] for base in sequence)
    
    # Reverse and return
    return complement[::-1]


def main():
    """
    Interactive command-line interface for the reverse complement tool.
    """
    print("DNA Reverse Complement Tool")
    print("=" * 30)
    print("Enter DNA sequences (A, T, G, C only)")
    print("Type 'quit' or 'exit' to stop\n")
    
    while True:
        try:
            # Get input from user
            sequence = input("Enter DNA sequence: ").strip()
            
            # Check for exit conditions
            if sequence.lower() in ['quit', 'exit', '']:
                print("Goodbye!")
                break
            
            # Calculate and display result
            reverse_comp = get_reverse_complement(sequence)
            print(f"Original:          5'-{sequence}-3'")
            print(f"Reverse complement: 3'-{reverse_comp}-5'")
            print()
            
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid DNA sequence using only A, T, G, C\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


# Example usage and testing
if __name__ == "__main__":
    # Run some test cases
    test_sequences = [
        "ATCG",
        "AAATTTGGGCCC",
        "GAATTC",  # EcoRI recognition site
        "AAGCTT",  # HindIII recognition site
        "atcg"     # lowercase test
    ]
    
    print("Test Results:")
    print("-" * 40)
    for seq in test_sequences:
        result = get_reverse_complement(seq)
        print(f"{seq:15} -> {result}")
    print()
    
    # Start interactive mode
    main()
