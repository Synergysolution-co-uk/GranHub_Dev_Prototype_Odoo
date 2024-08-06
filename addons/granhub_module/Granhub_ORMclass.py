from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a simple User model
Base = declarative_base()
#1
class User(Base):
    __tablename__ = 'Contents'

    id = Column(Integer, primary_key=True)
    Title = Column(String)
    Description = Column(String)
    Author = Column(String)
    ContentType = Column(String)
    EngagementMetrics = Column(String)
 #2   
class User(Base):
    __tablename__ = 'CommunityEvents'

    id = Column(Integer, primary_key=True)
    EventType = Column(String)
    EventDateTime = Column(String)
    Location = Column(String)
    MembershipDate = Column(String)
#3
class User(Base):
    __tablename__ = 'FamilyMembers'

    id = Column(Integer, primary_key=True)
    UserId = Column(String)
    Relationship = Column(String)
    ContactInformation = Column(String)
    SharedContent = Column(String)
    EventInvitations = Column(String)
    CommunicationHistory = Column(String)
 #4
 class User(Base):
    __tablename__ = 'Connections'

    id = Column(Integer, primary_key=True)
    UserId = Column(String)
    ConnectionUserId = Column(String)
    RelationshipType = Column(String)
    CommunicationHistory = Column(String)
    MessageThreads = Column(String)
    SocialNetworkinginteractions = Column(String)
 
 #5
    class User(Base):
    __tablename__ = 'SafetySettings'

    id = Column(Integer, primary_key=True)
    UserId = Column(String)
    PrivacySettings = Column(String)
    ConsentPreferences = Column(String)
    SecurityConfigurations = Column(String)
    SecurityEventLogs = Column(String)
    AuthenticationAteemptsLog = Column(String)
#6
class User(Base):
    __tablename__ = 'UserProfiles'

    id = Column(Integer, primary_key=True)
    UserId = Column(String)
    DateOfBirth = Column(String)
    Address = Column(String)
    LanguagePreference = Column(String)
    AccessibilitySettings = Column(String)
    NotificationPrefrences = Column(String)
#7
class User(Base):
    __tablename__ = 'Feedbacks'

    id = Column(Integer, primary_key=True)
    UserId = Column(String)
    FeedbackType = Column(String)
    FeedbackContent = Column(String)
    AnalysisReports = Column(String)
    ImprovementSuggestions = Column(String)
#8
class User(Base):
    __tablename__ = 'SupportTickets'

    id = Column(Integer, primary_key=True)
    UserId = Column(String)
    IssueDescription = Column(String)
    TroubleShootingSteps = Column(String)
    ResolutionDetails = Column(String)
    UserSatisfactionRating = Column(String)
#9
class User(Base):
    __tablename__ = 'Analytics'

    id = Column(Integer, primary_key=True)
    UserId = Column(String)
    UserActivityMetrics = Column(String)
    EngagementMetrics = Column(String)
    PerformanceIndicators = Column(String)
    AnalyticsReports = Column(String)
    Dashboards = Column(String)
    Insights = Column(String)
        
    
    

