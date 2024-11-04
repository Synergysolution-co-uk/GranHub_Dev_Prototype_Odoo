CREATE TABLE FamilymemberUserProfile (
    FamilymemberID INT,
    UserProfileID INT,
    PRIMARY KEY (FamilymemberID, UserProfileID),
    FOREIGN KEY (FamilymemberID) REFERENCES FamilyMembers(ID),
    FOREIGN KEY (UserProfileID) REFERENCES UserProfiles(ID)
);

CREATE TABLE SafetySettingsUserProfile (
    SafetySettingsID INT,
    UserProfileID INT,
    PRIMARY KEY (SafetySettingsID, UserProfileID),
    FOREIGN KEY (SafetySettingsID) REFERENCES SafetySettings(ID),
    FOREIGN KEY (UserProfileID) REFERENCES UserProfiles(ID)
);

CREATE TABLE FeedbackUserProfile (
    FeedbackID INT,
    UserProfileID INT,
    PRIMARY KEY (FeedbackID, UserProfileID),
    FOREIGN KEY (FeedbackID) REFERENCES Feedbacks(ID),
    FOREIGN KEY (UserProfileID) REFERENCES UserProfiles(ID)
);

CREATE TABLE SupportTicketsUserProfile (
    SupportTicketID INT,
    UserProfileID INT,
    PRIMARY KEY (SupportTicketID, UserProfileID),
    FOREIGN KEY (SupportTicketID) REFERENCES SupportTickets(ID),
    FOREIGN KEY (UserProfileID) REFERENCES UserProfiles(ID)
);

CREATE TABLE AnalyticsUserProfile (
    AnalyticsID INT,
    UserProfileID INT,
    PRIMARY KEY (AnalyticsID, UserProfileID),
    FOREIGN KEY (AnalyticsID) REFERENCES Analytics(ID),
    FOREIGN KEY (UserProfileID) REFERENCES UserProfiles(ID)
);