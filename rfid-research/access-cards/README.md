All access cards in this folder are real cards which will never be used in any operational deployment, or cards generated from those real cards.
Please feel free to use them to develop templates for your own custom cards.

Trying out Minimum, 1, and Maximum UID values could reveal defaults which were present in the system at time of installation but not properly removed.


==Understanding RFID Access Cards==

Access cards typically have two components - a serial number, and a facility code.

For example, let's take a look at one of the sample cards which we literally found in the middle of the road:
Key type: H10301
Data: 20 01 8A

All data is encoded in Hexidecimal format.
The first piece of data we can decode is the facility code, which in Hex format is 20.
Converting to Decimal, 20 becomes Facility Code 32.

Next we can examine the serial number. In this case, the serial number is as follows in Hex: 01 8A
When converted to decimal, this becomes serial number 394, which matches the 00394 serial number on the card.

We can now reverse engineer this in Flipper, and make our own cards.

So, if we wanted to gain access under someone else's card, all we need to do is view the back of their card, which has the serial number printed on it.
For example, if we look at someone else's card and it has 00123, we just need to adjust our Flipper generated card accordingly.
Facility code will stay at 32, so that converts to 20 in Hex.
Serial number 123 becomes 00 7B in Hex.
So our new card will need to have the data: 20 00 7B

Hope this helps understand the basics of access cards!
