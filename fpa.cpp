#include <iostream>
#include <cmath>
#include <bitset>
#include <iomanip>

struct FloatingPoint {
    // Sign (1 bit), Exponent (9 bits), Fraction (22 bits)
    int sign;
    int exponent;
    unsigned long long fraction; // large enough to handle the fraction plus any overflow

    FloatingPoint(float value) {
        // Decompose floating-point number into IEEE-like binary format
        if (value == 0.0f) {
            sign = 0;
            exponent = 0;
            fraction = 0;
            return;
        }

        sign = (value < 0) ? 1 : 0;
        value = fabs(value);

        int exp;
        float frac = std::frexp(value, &exp); // get fraction and exponent in IEEE 754 style
        exp += (1 << 8) - 1; // adjust exponent to fit in 9 bits (bias = 2^8 - 1)

        fraction = (unsigned long long)((frac - 0.5) * pow(2, 23)); // adjust fraction to 22 bits (+1 implicit leading one)

        exponent = exp;
    }

    std::string toBinaryString() const {
        // Construct binary string representation: 1 sign bit, 9 exponent bits, 22 fraction bits
        std::bitset<9> expBits(exponent);
        std::bitset<22> fracBits(fraction);
        return (sign ? "1" : "0") + expBits.to_string() + fracBits.to_string();
    }

    float toFloat() const {
        // Convert from binary format to float (inverse of constructor logic)
        float frac = (float)fraction / (1 << 22) + 0.5;
        int exp = exponent - (1 << 8) + 1;
        float value = std::ldexp(frac, exp);
        if (sign) value = -value;
        return value;
    }
};

FloatingPoint addFloatingPoints(const FloatingPoint& a, const FloatingPoint& b) {
    // A simple addition of two floating points in our custom format (ignores subnormal numbers, infinities, NaN)
    // Assumes exponents are aligned and no rounding is necessary for simplicity
    if (a.exponent > b.exponent) {
        // Align b with a
        return addFloatingPoints(b, a); // Make sure the larger exponent is first in the call
    }

    int expDiff = b.exponent - a.exponent;
    unsigned long long alignedFracA = a.fraction;
    alignedFracA >>= expDiff; // Shift fraction of a to align with b

    unsigned long long resultFraction = alignedFracA + b.fraction;
    int resultExponent = b.exponent;

    // Check for normalization and rounding needs
    bool needsNormalization = (resultFraction >> 22) > 0;
    if (needsNormalization) {
        resultFraction >>= 1; // Normalize
        resultExponent += 1;
    }

    // Rounding (simple round to nearest even, not implemented here for simplicity)
    bool needsRounding = false;

    return FloatingPoint{0, resultExponent, resultFraction};
}

int main() {
    float a, b;
    std::cout << "Enter two decimal numbers to add: ";
    std::cin >> a >> b;

    FloatingPoint fa(a), fb(b);

    std::cout << "Binary of first number: " << fa.toBinaryString() << " Decimal: " << fa.toFloat() << std::endl;
    std::cout << "Binary of second number: " << fb.toBinaryString() << " Decimal: " << fb.toFloat() << std::endl;

    FloatingPoint result = addFloatingPoints(fa, fb);
    std::cout << "Result in binary: " << result.toBinaryString() << std::endl;
    std::cout << "Result in decimal: " << result.toFloat() << std::endl;

    return 0;
}
