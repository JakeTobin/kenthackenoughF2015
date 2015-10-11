// This #include statement was automatically added by the Particle IDE.
#include "HttpClient/HttpClient.h"

// This #include statement was automatically added by the Particle IDE.
#include "InternetButton/InternetButton.h"

#include "InternetButton/InternetButton.h"

/* Here's a nice combination of features that I like to use.
Note the use of the allButtons function. */

InternetButton b = InternetButton();

bool rainbow_mode = true;

TCPClient client;







void setup() {
    // Tell b to get everything ready to go
    // Use b.begin(1); if you have the original SparkButton, which does not have a buzzer or a plastic enclosure
    // to use, just add a '1' between the parentheses in the code above.
    //String packet1 ="POST /button1  HTTP/1.1\r\nHost: 10.18.0.172:5000\r\nConnection: Close\r\nContent-Length: 0\r\nAccept: text/html\r\n";
    // packet = "POST " + "/add" + " HTTP/1.1\r\n";
    // packet += "Host: 10.18.0.172:5000\r\n";
    // packet += "Connection: Close\r\n";
    // packet += "Content-Length: 0\r\n";
    // packet += "Accept: text/html\r\n";



    // if(client.connect("10.18.0.172", 5000))
    // {
    // client.print(packet);
    // client.print("\r\n"); // Terminate the packet
    // }


    b.begin();
}

void loop(){


    // If this calls for a full spectrum situation, let's go rainbow!
    if(b.allButtonsOn()) {
        // Publish the event "allbuttons" for other services like IFTTT to use
        Spark.publish("allbuttons","allbuttons", 60, PRIVATE);
        b.rainbow(5);
        rainbow_mode = true;

        // If all buttons are on, don't try to process
        // the individual button responses below.  Just return.
        return;
    }

    // If we are not in rainbow mode anymore, turn the LEDs off
    if (rainbow_mode == true) {
        b.allLedsOff();
        rainbow_mode = false;
    }

    // Process individual buttons and LED response
    if (b.buttonOn(1)) {
        b.ledOn(12, 255, 0, 0); // Red
        b.rainbow(5);
        rainbow_mode = true;


        String packet1 ="POST /button1  HTTP/1.1\r\nHost: 10.18.0.172:5000\r\nConnection: Close\r\nContent-Length: 0\r\nAccept: text/html\r\n";

         if(client.connect("10.18.0.172", 5000))
    {
    client.print(packet1);
    client.print("\r\n"); // Terminate the packet
    }
        // Publish the event "button1" for other services like IFTTT to use
        Spark.publish("button1","button1", 60, PRIVATE);
        delay(500);
    }
    else {
        b.ledOn(12, 0, 0, 0);
    }

    if (b.buttonOn(2)) {
        b.ledOn(3, 0, 255, 0); // Green
        String packet2 ="POST /button2  HTTP/1.1\r\nHost: 10.18.0.172:5000\r\nConnection: Close\r\nContent-Length: 0\r\nAccept: text/html\r\n";

         if(client.connect("10.18.0.172", 5000))
    {
    client.print(packet2);
    client.print("\r\n"); // Terminate the packet
    }
        // Publish the event "button2" for other services like IFTTT to use
        Spark.publish("button2","button2", 60, PRIVATE);
        delay(500);
    }
    else {
        b.ledOn(3, 0, 0, 0);
    }

    if (b.buttonOn(3)) {
        b.ledOn(6, 0, 0, 255); // Blue
        String packet3 ="POST /button3  HTTP/1.1\r\nHost: 10.18.0.172:5000\r\nConnection: Close\r\nContent-Length: 0\r\nAccept: text/html\r\n";

         if(client.connect("10.18.0.172", 5000))
    {
    client.print(packet3);
    client.print("\r\n"); // Terminate the packet
    }
        // Publish the event "button3" for other services like IFTTT to use
        Spark.publish("button3","button3", 60, PRIVATE);
        delay(500);
    }
    else {
        b.ledOn(6, 0, 0, 0);
    }

    if (b.buttonOn(4)) {
        b.ledOn(9, 255, 0, 255); // Magenta
        String packet4 ="POST /button4  HTTP/1.1\r\nHost: 10.18.0.172:5000\r\nConnection: Close\r\nContent-Length: 0\r\nAccept: text/html\r\n";

         if(client.connect("10.18.0.172", 5000))
    {
    client.print(packet4);
    client.print("\r\n"); // Terminate the packet
    }
        // Publish the event "button4" for other services like IFTTT to use
        Spark.publish("button4","button4", 60, PRIVATE);
        delay(500);
    }
    else {
        b.ledOn(9, 0, 0, 0);
    }

    if(b.allButtonsOff()) {
        // Do something here when all buttons are off
         //b.allLedsOn( 0, 255, 0);

    }
}
