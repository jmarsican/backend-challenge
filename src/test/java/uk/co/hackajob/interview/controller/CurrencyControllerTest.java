package uk.co.hackajob.interview.controller;

import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
import uk.co.hackajob.interview.persistence.Country;
import uk.co.hackajob.interview.persistence.Currency;
import uk.co.hackajob.interview.persistence.repositories.CountryRepository;
import uk.co.hackajob.interview.persistence.repositories.CurrencyRepository;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest
@ContextConfiguration(classes = CurrencyController.class)
class CurrencyControllerTest {

    @MockBean
    private CountryRepository countryRepository;

    @MockBean
    private CurrencyRepository currencyRepository;

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void getCurrencyUsage() throws Exception {

        Mockito.when(countryRepository.findAll()).thenReturn(getCountries());

        mockMvc.perform(MockMvcRequestBuilders
                        .get("/currencies/usage")
                        .accept(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(MockMvcResultMatchers.jsonPath("$").exists())
                .andExpect(MockMvcResultMatchers.jsonPath("$").isArray())
                .andExpect(MockMvcResultMatchers.jsonPath("$.length()").value(2))
                .andExpect(MockMvcResultMatchers.jsonPath("$[0]").isNotEmpty())
                .andExpect(MockMvcResultMatchers.jsonPath("$[0].code").value("ABC"))
                .andExpect(MockMvcResultMatchers.jsonPath("$[0].name").value("A B C"))
                .andExpect(MockMvcResultMatchers.jsonPath("$[0].usages").value(1))
                .andExpect(MockMvcResultMatchers.jsonPath("$[0].countries").isArray())
                .andExpect(MockMvcResultMatchers.jsonPath("$[0].countries.length()").value(1))
                .andExpect(MockMvcResultMatchers.jsonPath("$[0].countries[0].iso3").value("CCN"))
                .andExpect(MockMvcResultMatchers.jsonPath("$[1]").isNotEmpty())
                .andExpect(MockMvcResultMatchers.jsonPath("$[1].code").value("DEF"))
                .andExpect(MockMvcResultMatchers.jsonPath("$[1].name").value("D E F"))
                .andExpect(MockMvcResultMatchers.jsonPath("$[1].usages").value(1))
                .andExpect(MockMvcResultMatchers.jsonPath("$[1].countries").isArray())
                .andExpect(MockMvcResultMatchers.jsonPath("$[1].countries.length()").value(1))
                .andExpect(MockMvcResultMatchers.jsonPath("$[1].countries[0].iso3").value("CCN"))
                .andExpect(MockMvcResultMatchers.jsonPath("$[1].usages").value(1))

        ;
    }

    private List<Country> getCountries() {
        List<Country> list = new ArrayList<>();
        Currency c = new Currency();
        c.setCode("ABC");
        c.setName("A B C");

        Currency c2 = new Currency();
        c2.setCode("DEF");
        c2.setName("D E F");

        Country country = new Country();
        country.setCca3("CCN");
        country.setCommonName("Country Common Name");
        country.addCurrency(c);
        country.addCurrency(c2);

        list.add(country);
        return list;
    }
}