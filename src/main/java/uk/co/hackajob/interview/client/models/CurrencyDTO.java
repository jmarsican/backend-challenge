package uk.co.hackajob.interview.client.models;

public class CurrencyDTO {

    private String name;
    private String symbol;

    // - - - - - - - - - -
    // - - - - - - - - - -

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    @Override
    public String toString() {
        return "CurrencyDTO{" +
                "name='" + name + '\'' +
                ", symbol='" + symbol + '\'' +
                '}';
    }
}
