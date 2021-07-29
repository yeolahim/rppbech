#include <pico/stdlib.h>

int main() {
    const uint LED_PIN0 = PICO_DEFAULT_LED_PIN;
    const uint LED_PIN1 = 14;
    const uint LED_PIN2 = 17;
    gpio_init(LED_PIN0);
    gpio_set_dir(LED_PIN0, GPIO_OUT);
    gpio_init(LED_PIN1);
    gpio_set_dir(LED_PIN1, GPIO_OUT);
    gpio_init(LED_PIN2);
    gpio_set_dir(LED_PIN2, GPIO_OUT);
    while (true) {
        gpio_put(LED_PIN0, 1);
        sleep_ms(50);
        gpio_put(LED_PIN0, 0);
        sleep_ms(50);
        //
        gpio_put(LED_PIN1, 1);
        sleep_ms(200);
        gpio_put(LED_PIN1, 0);
        sleep_ms(200);
        //
        gpio_put(LED_PIN2, 1);
        sleep_ms(100);
        gpio_put(LED_PIN2, 0);
        sleep_ms(100);
    }
}
