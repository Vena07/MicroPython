import machine



# Definuje proměnnou led1 jako výstupní pin na GPIO pinu 1      
led = machine.Pin(1,machine.Pin.OUT)


#S funkcí value() s vnitří hodnotou 1 led_dioda bude svítí
led.value(1)

#S funkcí value() s vnitří hodnotou 0 led_dioda nebude svítí
led.value(0)