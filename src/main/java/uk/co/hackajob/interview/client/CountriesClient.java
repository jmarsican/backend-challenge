package uk.co.hackajob.interview.client;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;
import uk.co.hackajob.interview.client.models.CountryDTO;

import java.util.Set;

@Component
public class CountriesClient {

    protected final Log LOG = LogFactory.getLog(getClass());

    private static final String URL = "https://s3.eu-west-1.amazonaws.com/hackajob-assets1.p.hackajob/challenges/global_currency_usage/index.json";

    public Set<CountryDTO> getCountries() {

        WebClient client = WebClient.create();

        Mono<Set<CountryDTO>> response = client
                .get()
                .uri(URL)
                .retrieve()
                .bodyToMono(new ParameterizedTypeReference<Set<CountryDTO>>() {})
                .log();

        return response.block();

    }

}
