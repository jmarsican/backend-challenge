package uk.co.hackajob.interview;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.PropertySource;
import uk.co.hackajob.interview.client.CountriesClient;
import uk.co.hackajob.interview.persistence.repositories.CountryRepository;

@SpringBootApplication(scanBasePackages = {"uk.co.hackajob"})
@PropertySource(value = {"application.properties"})
public class GlobalCurrenciesApplication {

	private static final Logger LOG = LoggerFactory.getLogger(GlobalCurrenciesApplication.class);

	@Bean
	@Autowired
	public DataInitialiser schedulerRunner(CountriesClient countriesClient,
										   CountryRepository countryRepository) {
		return new DataInitialiser(countriesClient, countryRepository);
	}

	public static void main(String[] args) {

		new SpringApplicationBuilder()
				.sources(GlobalCurrenciesApplication.class)
				.web(WebApplicationType.SERVLET)
				.run(args);
		
	}

}
