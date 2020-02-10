# bloomon

### technical challenge

Full requirements are in the file **requirements.pdf**

## run instructions
Docker is required to run the code.
Test data should be sent to standard input. The result is sent to standard output.
See the example below. sample.txt is an example file.

    git clone https://github.com/eugene-kuchansky/flowers.git bloomon-test-ek
    cd test-ek
    docker build -t bloomon-test-ek .
    docker run --rm -i bloomon-test-ek < sample.txt


# implementation
The main idea was to create a minimal working prototype with a reasonable number of abstraction layers.

    
# important notes
Developing took more than 4 hours to complete. Additional time was required to demonstrate the ideas behind the code.

So out of scope of 4 hours:

- most of the tests
- most of the type annotations
- comments and docstrings
- this document


# planned but not implemented things

1. The bouquet composer module was planned to be replaceable so it consists of 2 parts: abstract class and one implementation.
The only implementation is naive - as soon as it possible to create a bouquet it is created.
So in case when there are 2 designs AS1a2 and AS10a10 the second one never be created.

2. In the naive implementation, the missing part is caching.
Every time a new flower is added all suitable bouquets are checked once again.

3. The initial plan was to create a more sophisticated Composer.
Every design would have a priority. The more times bouquet is created the lower priority in flowers sorting it has.

4. The other potential implementation was in mind if the storage allows keeping a huge number of flowers before creating bouquets.
In this case, it would be possible to maximize the number of bouquets, maximize revenue or minimize the balance of unused flowers.

5. Some code still has to be extracted to separate classes.

6. Base Python data types such as lists, dicts have to be replaced with abstractions in the case when they used as transmitted data between layers.

7. More tests required

8. Logging should be added to all processes.

9. Verification of incoming data and fault tolerance.
 
10. Scaling and distribution across a cluster in case of high load.
