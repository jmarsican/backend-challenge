package uk.co.hackajob.interview.client.models;

public class NameDTO {

    private String common;
    private String official;

    // - - - - - - - - - -
    // - - - - - - - - - - 

    public String getCommon() {
        return common;
    }

    public void setCommon(String common) {
        this.common = common;
    }

    public String getOfficial() {
        return official;
    }

    public void setOfficial(String official) {
        this.official = official;
    }

    @Override
    public String toString() {
        return "NameDTO{" +
                "common='" + common + '\'' +
                ", official='" + official + '\'' +
                '}';
    }
}
