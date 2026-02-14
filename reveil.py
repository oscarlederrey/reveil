import max7219
display = max7219.SevenSegment(digits=4, scan_digits=8, cs=4, spi_bus=6, reverse=True)
display.text("ABCDEF")
display.number(3.14159)
display.message("Hello World")
display.clear()