package uk.co.hackajob.interview;

import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.PropertySource;

@SpringBootApplication(scanBasePackages = {"uk.co.hackajob"})
@PropertySource(value = {"application.properties"})
public class GlobalCurrenciesApplication {

	@Bean
	public DataInitialiser schedulerRunner() {
		return new DataInitialiser();
	}

	public static void main(String[] args) {

		new SpringApplicationBuilder()
				.sources(GlobalCurrenciesApplication.class)
				.web(WebApplicationType.SERVLET)
				.run(args);
		
	}

}
