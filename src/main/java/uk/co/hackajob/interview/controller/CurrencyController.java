package uk.co.hackajob.interview.controller;

import org.springframework.http.MediaType;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.ResponseStatus;

import java.util.Collections;
import java.util.List;

@CrossOrigin(origins = "*", allowedHeaders = "*")
@RestController
@RequestMapping(value = "/currencies")
@ResponseStatus(code = HttpStatus.NOT_FOUND, reason = "API not implemented yet")
public class CurrencyController {
    
    @RequestMapping(value = "/usage", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
    public List<?> getCurrencyUsage() {

        // implement your code here to retrieve the data that was stored in the database
        // using the DataInitialiser and  return it in JSON format

        return Collections.emptyList();
    }
}
