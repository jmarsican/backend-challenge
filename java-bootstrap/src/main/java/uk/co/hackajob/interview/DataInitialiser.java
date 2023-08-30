package uk.co.hackajob.interview;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;

public class DataInitialiser implements CommandLineRunner {

    @Autowired
    public DataInitialiser() {
        // Autowire any beans that you create and
        // use to capture and store data from the public API endpoint
    }

    @Override
    public void run(String... args) throws Exception {
        // implement code to capture and store data from the public API endpoint
    }
    
}